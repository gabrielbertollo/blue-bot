import discord
import os
import random
import requests
import json
from requests.models import HTTPBasicAuth

client = discord.Client()

auth_params = {
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('SECRET'),
    'grant_type': 'client_credentials'
}


twitch_url = 'https://twitch.tv/blue_nysa'
love_emote = '<:blue_love_emote:875531652795883551>'
haha_emote = '<:blue_haha_emote:841854651779121192>'
blue_user = '<@!478694253460062248>'
live_messages = [
    '@everyone A ' + blue_user + ' está ao vivo! Vem conversar com a gente! ' +
    love_emote + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' tá ON pessoal! Cola lá! ' +
    love_emote + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' está ao vivo! ' +
    love_emote + ' Boraa' + '\n' + twitch_url,
    '@everyone A ' + blue_user + ' tá OOONN!!! Corre lá!\n' + twitch_url,
    '@everyone vocês não vão acreditar! A LIVE COMEÇOU! ' +
    haha_emote + '\n' + twitch_url,
]


def check_twitch():
    url = 'https://api.twitch.tv/helix/streams?user_login=blue_nysa'
    authURL = 'https://id.twitch.tv/oauth2/token'

    auth_call = requests.post(url=authURL, params=auth_params)
    access_token = auth_call.json()['access_token']

    header = {
        'Client-ID': os.getenv('CLIENT_ID'),
        'Authorization':  "Bearer " + access_token
    }

    response = requests.get(url, headers=header).json()['data']

    if response:
        response = response[0]
        if response['type'] == 'live':
            return True
        else:
            return False
    else:
        return False


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
        if check_twitch():
            await message.channel.send(random.choice(live_messages))
        else:
            await message.channel.send('Parece que a ' + blue_user + ' não está ao vivo agora...')


client.run(os.getenv('TOKEN'))
