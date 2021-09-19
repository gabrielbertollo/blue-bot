import discord
import os
import random

client = discord.Client()

twitch_url = 'https://twitch.tv/blue_nysa'
love_emote = '<:blue_love_emote:875531652795883551>'
haha_emote = '<:blue_haha_emote:841854651779121192>'
blue_user = '<@!478694253460062248>'
live_messages = [
    '@everyone A ' + blue_user + ' está ao vivo! Vem conversar com a gente! ' +
    love_emote + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' tá ON pessoal! Cola lá! ' + love_emote + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' está ao vivo! ' +
    love_emote + ' Boraa' + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' tá OOONN!!! Corre lá!\n' + twitch_url, 
    '@everyone vocês não vão acreditar! A LIVE COMEÇOU! ' + haha_emote + '\n' + twitch_url,
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$oi'):
        await message.channel.send('Oie, eu sou a BlueBot! <:blue_love_emote:875531652795883551>')

    if message.content.startswith('$live'):
        await message.channel.send(random.choice(live_messages))

client.run(os.getenv('TOKEN'))
