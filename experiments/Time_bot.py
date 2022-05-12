#This code will not run even with proper modifications. The readme includes the proper
#modifications.

#Written by Stefan X. Strutz on May 1, 2022, last updated on May 9, 2022
#The purpose of this code is to test interactions between the time and discord module.

#Changed during the function to be message triggered and set time specified in message

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

# All functions must be triggered by messages as the code can only have one event loop.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!time'):
        await message.channel.send(time.ctime())

    if message.content.startswith('!hour'):
        await message.channel.send(time.localtime().tm_hour)
    try:  
        if message.content.startswith('!ding'):
            ding_at = int(message.content[6:8])
            not_dinged = True
            while not_dinged:
                channel = client.get_channel(Channel_number_here)#replace 
                if time.localtime().tm_min==ding_at:
                        await channel.send('ding')
                        not_dinged =False
                else:
                    await asyncio.sleep(24)
                    #await channel.send('dong') # print debug
    except:
         channel = client.get_channel(Channel_number_here)#replace 
         await channel.send("Command must be used in the form !ding ## where the #'s are numbers'")


#Starts the event loop.
client.run('bot_token_here') #replace

 

