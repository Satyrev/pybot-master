import discord
import random
import os
import time
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '~')

#test

#===================================
#events
#===================================

client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity = discord.Streaming(name = "you dying to a bot", url = "")) #put twitch url

@client.event
async def on_member_join(member):
    embedVar = discord.Embed(description=f'Welcome to the server {member.mention}', color=0xD40000)
    channel = discord.utils.get(member.guild.channels, name="📀│welcome") #path where the bot sends welcome message
    await channel.send(embed=embedVar)
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(role)

#@client.event
#async def on_message_delete(message):
#    if message.author.id == (): #Checks the ID, if AuthorID = BotID, return. Else, continue. Add discord id here
#        author : message.author #Defines the message author
#        content : message.content #Defines the message content
#        channel : message.channel #Defines the message channel
#       logchannel = discord.utils.get(message.guild.channels, name='message-deletes') #Defines the logs channel
#        await logchannel.send(channel, '{}: {}'.format(author, content)) #Send the message.

#@client.event
#async def on_message_delete(message):
#    embedVar = discord.Embed(title="Message Deleted", color=0xf40000)
#    embedVar.add_field(name="Before", value=message.content + ": was Deleted!", inline=False)
#    channel = discord.utils.get(message.guild.channels, name="message-deletes")
#    await channel.send(embed=embedVar)

#@bot.event
#async def on_message(message: str):
#    ts = time.time()
#    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#    with open("logs.txt", "a") as text_file:
#    print(f"<{st}> {message.content}", file=text_file)

#@client.event
#async def on_member_join(member):
#    await member.send("Welcome, please read the rules.")

#@client.event
#async def on_member_join(member):
#    print(f'{member} has joined a server.')

#@client.event
#async def on_member_remove(member):
#    print(f'{member} has left a server.')

#@client.event
#async def on_message_delete(message):
#    print(f'{message} - message deleted')

@client.event
async def on_member_remove(member):
    embedVar = discord.Embed(description=f':outbox_tray:{member.mention}**left the server**', color=0xD40000)
    embedVar.add_field(name="‎‎", value=member.id)
    embedVar.set_author(name=f'{member}')    
    embedVar.set_footer(text=f'{member.joined_at.strftime("%a, %#d %B %Y, %Y, %I:%M %p UTC")}')
    embedVar.set_thumbnail(url=member.avatar_url)
    channel = discord.utils.get(member.guild.channels, name="bot-logs") #path where bot sends leave message
    await channel.send(embed=embedVar)

#@client.event
#async def on_member_join(member):
#    channel = discord.utils.get(member.guild.channels, name="test1")
#    member_count = len(message.guild.members)
#    new_name = (f"{member_count}") #bad server info updater probably doesnt work
#    await channel.edit(name=new_name)

#@client.event
#async def on_member_join(member):
#    channel = discord.utils.get(member.guild.channels, name=) #discord id here
#    new_name = (f'{guild.members}') #bad server info updater probably doesnt work - 2
#    await channel.edit(name=new_name)

#===================================
#fun commands
#===================================

@client.command()
async def test(ctx):
        embedVar = discord.Embed(title="kick", description="Desc", color=0xD40000)
        await ctx.send(embed=embedVar)

@client.command()
async def ping(ctx):
    """Shows the server ping"""
    embedVar = discord.Embed(description=f'PyBots ping is {round(client.latency *1000)}ms', color=0xD40000)
    await ctx.send(embed=embedVar)

@client.command(aliases=['8ball'])
@commands.has_permissions(administrator=True)
async def _8ball(ctx,*, question):
    """.8ball (question) - answers a yes or no question"""
    responses = ['As I see it, yes',
                 'Most likely',
                 'Don’t count on it',
                 'My sources say no',
                 'Very doubtful',
                 'It is certain',
                 'Ask again later']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def add(ctx, first: int, second: int):
    """.add (number) (number)"""
    embedVar = discord.Embed(description=f'{first + second}', color=0xD40000)
    await ctx.send(embed=embedVar)

@client.command()
async def multiply(ctx, first: int, second: int):
    """.multiply (number) (number)"""
    embedVar = discord.Embed(description=f'{first * second}', color=0xD40000)
    await ctx.send(embed=embedVar)

@client.command()
async def divide(ctx, first: int, second: int):
    """.divide (number) (number)"""
    embedVar = discord.Embed(description=f'{first / second}', color=0xD40000)
    await ctx.send(embed=embedVar)

@client.command()
async def square(ctx, first: int, second: int):
    """.square (number) (number)"""
    embedVar = discord.Embed(description=f'{first * second}', color=0xD40000)
    await ctx.send(embed=embedVar)

@client.command()
async def choose(ctx, *choices: str):
    """.choose (option1) (option2) -  chooses"""
    embedVar = discord.Embed(description=random.choice(choices), color=0xD40000)
    await ctx.send(embed=embedVar)

#@client.command()
#async def unoblock(ctx):
#    """UNOBLOCK"""
#    await ctx.send(f'https://i.pinimg.com/170x/fa/7c/35/fa7c35a3d7b4e03bc72c1498cc9d9add.jpg')

#@client.command()
#async def unoreverse(ctx):
#    """UNOREVERSE"""
#    await ctx.send(f'https://i.pinimg.com/736x/5e/14/74/5e1474e0f4edcf26c0277310b41c0adb.jpg')

@client.command()
async def roulette(ctx, reason=None):
    responses = ["click", "click", "click", "click", "click", "BANG"]
    random_response = random.choice(responses)
    if random_response == "BANG":
        embedVar = discord.Embed(titel="LOL CLAPPED", description=f'I have some good news and bad news, the good news is {ctx.message.author.mention} is gone. The bad news is... wait, there is no bad news.', color=0xD25959)
        await ctx.message.author.ban(reason=reason)
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(description=f'{ctx.message.author.mention}, the odds were in your favor.', color=0xC99E1A)
        role = discord.utils.get(ctx.guild.roles, name="Crazy Russian") #role added after roulette
        await ctx.message.author.add_roles(role)
        await ctx.send(embed=embedVar)

#===================================
#moderation commands
#===================================

@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Moderation", description="`~helpAdmin` - Get info on Moderation Commands", color=0x00ff00)
    embedVar.add_field(name="Fun", value="`~helpFun` - Get info on Fun Commands", inline=False)
    embedVar.add_field(name="Automod", value="`~helpAutomod` - Blacklist Words!", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
async def helpAdmin(ctx):
    embedVar = discord.Embed(title="Moderation", description="`~clear number`- Clears messages\n `~kick @someone`\n `~ban @someone`\n `~unban someone#0000`\n `~freeze`- Makes the text channel Admin only\n `~melt`- Unfreezes channel\n `~mute @someone`- Set Muted role\n `~unmute @someone`\n `~admin @someone`- Adds role Admin\n `~unadmin @someone`- Command Owner only\n `~userinfo @someone`-Sends user info in chat\n `~setdelay (seconds)`- Sets slowmode for channel\n `~tempmuteseconds @someone`- Sets role Muted for number of seconds\n `~tempmuteminutes @someone`- Sets role Muted for number of minutes\n `~tempmutehours @someone`- Sets role Muted for number of hours\n `~warn1 @someone` (warns)\n `~warn2 @someone` (warns and mutes for 30 mins)\n `~warn3 @someone` (warns and mutes for 24 hours)\n `~clearwarn1 @someone`- Deletes role\n `~clearwarn2 @someone`- Deletes role warn2 from user\n `~clearwarn3 @someone`- Deletes role warn3 from user\n `~clearwarnsall @someone`- Clears all warns", color=0x00ff00)
    await ctx.send(embed=embedVar)

@client.command()
async def helpFun(ctx):
    embedVar = discord.Embed(title="Fun", description="`~ping`\n `~8ball` (question)\n `~add number1 number2` add\n `~multiply number1 number2` multiply\n `~divide number1 number2` divide\n `~square number1 number2` square\n `~choose option1 option2` chooses from two options\n `~roulette` 1/6 chance of getting banned", color=0x00ff00)
    await ctx.send(embed=embedVar)

@client.command()
async def helpAutomod(ctx):
    embedVar = discord.Embed(title="Automod", description="`Blacklist words` this has to be added into the code manually", color=0x00ff00)
    await ctx.send(embed=embedVar)
  
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    """.clear (number of messages) - clears messages"""
    await ctx.channel.purge(limit=amount+1)
    embedVar = discord.Embed(description=f'Cleared {amount} Messages', color=0xD40000)
    message = await ctx.send(embed=embedVar)
    await asyncio.sleep(2)
    await message.delete()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    """.kick @someone - kicks member"""
    embedVar = discord.Embed(title="User Kicked", description=f'Kicked {member.mention}', color=0xD40000)
    await member.kick(reason=reason)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    """.ban @someone - bans member"""
    embedVar = discord.Embed(title="User Banned", description=f'Banned {member.mention}', color=0xD40000)
    await member.ban(reason=reason)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    """.unban someone#0000 - unbans user"""
    embedVar = discord.Embed(title="User Unbanned", description=f'Unbanned', color=0xD40000)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=embedVar)
            return

@client.command()
@commands.has_permissions(administrator=True)
async def freeze(ctx):
        embedVar = discord.Embed(title="Channel Frozen", description=f'Channel frozen! Only users/roles with explicit permission to speak may speak in this channel', color=0xD40000)
        """.freeze - freezes the chat, only admins will talk"""
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def melt(ctx):
        """.melt - unfreezes the chat"""
        embedVar = discord.Embed(title="Channel Melted", description=f'Channel melted, everyone can talk', color=0xD40000)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    """.mute @someone - mutes user"""
    embedVar = discord.Embed(title="User Muted", description=f'Muted', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def tempmuteseconds(ctx, mute_time : int, member: discord.Member=None):
    """.mute @someone - mutes user"""
    embedVar = discord.Embed(title="User Muted", description=f'Muted for {mute_time} seconds', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(embed=embedVar)
    embedVar = discord.Embed(title="User Unmuted", description=f'Time is up', color=0xD40000)
    await asyncio.sleep(mute_time)
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def tempmuteminutes(ctx, mute_time : int, member: discord.Member=None):
    """.mute @someone - mutes user"""
    embedVar = discord.Embed(title="User Muted", description=f'Muted for {mute_time} minutes', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(embed=embedVar)
    embedVar = discord.Embed(title="User Unmuted", description=f'Time is up', color=0xD40000)
    await asyncio.sleep(mute_time * 60)
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def tempmutehours(ctx, mute_time : int, member: discord.Member=None):
    """.mute @someone - mutes user"""
    embedVar = discord.Embed(title="User Muted", description=f'Muted for {mute_time} hours', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(embed=embedVar)
    embedVar = discord.Embed(title="User Unmuted", description=f'Time is up', color=0xD40000)
    await asyncio.sleep(mute_time * 3600)
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    """.unmute @someone - unmutes the user"""
    embedVar = discord.Embed(title="User Unmuted", description=f'Unmuted', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def admin(ctx, member: discord.Member=None):
    """.admin @someone - makes a user admin"""
    embedVar = discord.Embed(title="Admin Added", description=f'User is now an admin', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Admins")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_role("gamer")
async def unadmin(ctx, member: discord.Member=None):
    """.unadmin @someone - removes admin from user"""
    embedVar = discord.Embed(title="Admin Revoked", description=f'User is no longer an admin', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Admins")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def warn1(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warned", description=f'User warned', color=0xD40000)
    role1 = discord.utils.get(ctx.guild.roles, name="Warn 1")
    await member.add_roles(role1)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def warn2(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warned", description=f'User warned', color=0xD40000)
    role1 = discord.utils.get(ctx.guild.roles, name="Warn 2")
    await member.add_roles(role1)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(embed=embedVar)
    embedVar1 = discord.Embed(title="User Unmuted", description=f'Time is up', color=0xD40000)
    await asyncio.sleep(30 * 60)
    await member.remove_roles(role)
    await ctx.send(embed=embedVar1)

@client.command()
@commands.has_permissions(administrator=True)
async def warn3(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warned", description=f'User warned', color=0xD40000)
    role1 = discord.utils.get(ctx.guild.roles, name="Warn 3")
    await member.add_roles(role1)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(embed=embedVar)
    embedVar1 = discord.Embed(title="User Unmuted", description=f'Time is up', color=0xD40000)
    await asyncio.sleep(24 * 3600)
    await member.remove_roles(role)
    await ctx.send(embed=embedVar1)

@client.command()
@commands.has_permissions(administrator=True)
async def clearwarn1(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warn 1 cleared", description=f'Warn 1 removed', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Warn 1")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def clearwarn2(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warn 2 cleared", description=f'Warn 2 removed', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Warn 2")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def clearwarn3(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warn 3 cleared", description=f'Warn 3 removed', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Warn 3")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def clearwarnall(ctx, member: discord.Member=None):
    embedVar = discord.Embed(title="Warns cleared", description=f'User pardoned', color=0xD40000)
    role = discord.utils.get(ctx.guild.roles, name="Warn 1")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)
    role = discord.utils.get(ctx.guild.roles, name="Warn 2")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)
    role = discord.utils.get(ctx.guild.roles, name="Warn 3")
    await member.remove_roles(role)
    await ctx.send(embed=embedVar)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    
    embedVar = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embedVar.set_author(name=f'User Info - {member}')
    embedVar.set_thumbnail(url=member.avatar_url)
    embedVar.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embedVar.add_field(name="ID:", value=member.id)
    embedVar.add_field(name="Guild name:", value=member.display_name)

    embedVar.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embedVar.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %Y, %I:%M %p UTC"))
    
    embedVar.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
    embedVar.add_field(name="Top role:", value=member.top_role.mention)

    embedVar.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embedVar)

@client.command()
async def setdelay(ctx, seconds: int):
    embedVar = discord.Embed(title="Slowmode Activated", description=f"Set the slowmode delay in this channel to {seconds} seconds", color=0xD40000)
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(embed=embedVar)

#===================================
#auto
#===================================

@client.event
async def on_message(message):
    bad_words = ['FILTERWORD1', 'FILTERWORD2'] #add or change this to filter words
    user = client.get_user(703848463615393862)
    embedVar = discord.Embed(title="Blacklisted Word", description=f'Blacklisted word mentioned **deleting message**', color=0xD40000)
    for word in bad_words:
        if 0 < message.content.count(word) < 2:
            print("someone tried saying a blacklisted word")
            await message.channel.send(embed=embedVar) #message sent when filter word is said
            await message.delete() #message gets deleted
            break
    else:
        await client.process_commands(message)
    
#===================================
#changelog
#===================================


@client.command()
async def changelog(ctx):
    """.changelog - shows the changelog"""
    embedVar = discord.Embed(title="Changelog", color=0xD40000)
    embedVar.add_field(name="1", value=f'Fixed minor bugs, revamped `help` command, changed AutoMod to use embeds', inline=False)
    await ctx.send(embed=embedVar)

client.run(os.environ['DISCORD_TOKEN'])