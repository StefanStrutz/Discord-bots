#This code will not run unless it is modified, see readme document

#Code written by Stefan X. Strutz, parts are based on a tutorial that whose origin I forgot
#Comments added on 4/24/2022,  original code written in January of the same year

#This was my 1st discord bot and my 1st Python code.it is nice to get it working,
#but I realized I was going to need a web course to teach me some of the finer points of Python.


import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    channel = client.get_channel(Channel_number_here)#replace 
    await channel.send('hello')
   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fuzz'):
        await message.channel.send('buzz')

    if message.author.id == user_ID_here: #replace
        if message.content.startswith('sleep bot'):
            await message.channel.send('bye')
            exit()#this doesn't quite work as intended as you have to click yes on a box that pops up
            return
        return


client.run('bot_token_here') #replace 
