import os, pytz
import random, math, discord, datetime
from discord.ext import commands
from discord.ext.commands import MemberConverter
import datetime
import news


# Authentication
TOKEN =''   # This information is only available to the creator of this project

# creating bot object
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.lower() == "who is usf-helper?":
        await message.channel.send(f"Hello {message.author.display_name}! I am USF-HELPER, your Discord Bot that is going to make your USF expirience better!")

    if "show usf news" == message.content.lower():
        await message.channel.send(f"I found the following information on https://www.usf.edu/news/listing.aspx: {news.Infogetter().usf()}")

    if "usf-helper documentation" == message.content.lower():
        await message.channel.send("""Documentation:
        To use any of the following commands you have to type them in your messages

        Commands: (all of the commands are case insensative)
        1. who is usf-helper? --- desribes the basic functions of the bot
        2. show usf news --- shows the latest USF news (give the bot 10 seconds to find the information)
        3. usf-helper documentation --- Shows the documentation
        4. contribute --- Lets the users contribute to the project
        5. contact advisors --- lists contact information of cs advisors
        6. usf cs undergraduate webpage --- redirects you to the usf cs undergraduate webpage
        7, usf cs student outcomes --- redirects you to the usf cs student outcome webpage
        8. usf enrollment data --- redirects you to the usf enrollment data webpage
        9. usf cs outstanding graduates --- redirects you to the usf cs outstanding graduates webpage
        10. usf cs research --- redirect you to the usf research webpage
        11. time in florida --- shows local Florida time


        Actions:
        1. Notifies if someone changes a message
        2. Notifies if someone deletes a message
        3. Greeds new memebers
        4. Notifies if a person left the server

        Note: Feel free to ask the creator of this project to change/add/delete any of the commands or actions
         """)

    if "contribute" == message.content.lower():
        await message.channel.send(f"If you have great programming skills, you can go to https://github.com/azimIbragimov/USF-HELPER and directly contribute to the project. \nBut if you are still learning the basics of programming, you can provide your ideas and suggestions to Azim Ibragimov")

    if message.content.lower() == "contact advisors":
        await message.channel.send("""This information is taken from https://www.usf.edu/engineering/cse/undergraduate/contacts.aspx:
        John Morgan, Email: jpmorga2@usf.edu
        Marjorie Fontalvo: mfontalv@usf.edu
        Mayra Morfin: mayra1@usf.edu
        Also, you should remember that if you want to make an appoint with them, you should do so in Archivium""")

    if message.content.lower() == "usf cs undergraduate webpage":
        await message.channel.send(f"You can find more information here: https://www.usf.edu/engineering/cse/undergraduate/ug-announcements.aspx")

    if message.content.lower() == "usf cs student outcomes":
        await message.channel.send(f"You can find more information here: https://www.usf.edu/engineering/cse/about/student-outcomes.aspx")

    if message.content.lower() == "usf enrollment data":
        await message.channel.send(f"You can find more information here: https://www.usf.edu/engineering/cse/about/enrollment-trends.aspx")

    if message.content.lower() == "usf cs outstanding graduates":
        await message.channel.send(f"You can find more information here: https://www.usf.edu/engineering/cse/about/outstanding-graduates.aspx")

    if message.content.lower() == "usf cs research":
        await message.channel.send(f"You can find more information here: https://www.usf.edu/engineering/cse/research/index.aspx")

    if message.content.lower() == 'time in florida':
        tz = pytz.timezone("EST")
        await message.channel.send(f"It is {datetime.datetime.now(tz).strftime('%H:%M:%S')} in florida")





@client.event
async def on_message_delete(message):
        await message.channel.send(f"Should I notify all of you when {message.author.display_name} deletes a message?")

@client.event
async def on_message_edit(before, after):
        await after.channel.send(f"Should I notify all of you when {after.author.display_name} edits a message? ")

@client.event
async def on_member_join(member):
        channel = discord.utils.get(member.guild.channels, name='general')
        await channel.send(f":smiley::smiley::smiley:\nHello, {member.nick}! " +
        """\n Welcome to the USF's Computer Science Discord Chat!
         Here you can chat with other Computer Science Students, ask questions about the USF, and find new friends!
         You can find some information about other students in the #welcome channel, and, if you want to, you can share some information about yourself with other people!
         Also, you can find picutres of other students in #face-reveals channel, and you are welcome to share your picutres on that channel if you want to!
         Welcome to the community of fellow programmers!""")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f"Oh no! {member} has left the chat :cry:")




client.run(TOKEN)
