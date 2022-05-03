#This code will not run even with proper modifications. The readme includes the proper
#modifications.

#Written by Stefan X. Strutz on May 1, 2022
#The genreal purpose of the time bought is to test interactions between the time and
#discord module.

#For my 1st attempt I was trying to make a bot that would say ding at a specific minute.
#I discovered that the asynchronous module can only have one event loop.

#It explains why a lot of functions using asynchronous module have a main function.
#Any loop only to be contained in the discord client loop with a @client.event before
#it. Since the discord modules based on events, I'll have to the start the timecode with 
#a discord message

import discord
import time
import asyncio #This is probably a super of discord, but there are some functions I
# want from it and I don't want to find out discord doesn't have them.



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(Channel_number_here)#replace 
    await channel.send('hello')

#No point in a time-based discord bot if the time part breaks normal bot functions.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!time'):
        await message.channel.send(time.ctime())

    if message.content.startswith('!hour'):
        await message.channel.send(time.localtime().tm_hour)
        
async def check_time():
    while True:
        if time.localtime().tm_min==35:
                channel = client.get_channel(Channel_number_here)#replace 
                await channel.send('ding')
        else:
            await asyncio.sleep(24)

async def launch():
    client.run('bot_token_here') #replace 

#The failures are located here as both of these count as event loops.
asyncio.run(launch())
asyncio.run(check_time())
    





