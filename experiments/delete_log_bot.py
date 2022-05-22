#This code will not run unless it is modified, see readme document

#Written by Stefan X. Strutz on May 21, 2022, 
#the purpose of this code is to test interactions between the OS and discord module


import discord
import os
import asyncio

def log_append(msg):
    stream = open ("deleted_log.txt","a")
    stream.write (msg)
    stream.close
    

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(Channel_number_here)#replace 
    await channel.send('Ready to snitch.')

@client.event
async def on_message_delete(message):
        msg = f'{message.author} has deleted the message: {message.content}'
        log_append(msg+"\n")
        await asyncio.sleep(1) #there might be a better way to have this await do nothing


client.run('bot_token_here') #replace
