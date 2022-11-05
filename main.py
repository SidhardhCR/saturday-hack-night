import discord
import random
import requests
import json
from keep_alive import keep_alive
Token = 'MTAzODQ1MzM1MDkxNzczNDQwMA.GpGN8_.XACQr3p_Ca-DdRi7f6cI7tVhC3s6FZ4ZN2qYbA'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

sad_words =['sad','depressed','depression','unhappy','angry','alone']
joke_words=['joke','tell me a joke','jokes']
encoraging_words = ['cheer up!','you are a good person /bot','Dont give up','Stay strong','Come on! You can do it!.']
jokes=['Why don’t pirates take a shower before they walk the plank? \nThey just wash up on shore.','Why did an old man fall in a well?\nBecause he couldn’t see that well!'
,'Why did a scarecrow win a Nobel prize?\nHe was outstanding in his field!','What’s the difference between a hippo and a Zippo?\nOne is very heavy, the other is a little lighter!']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



def get_quote():
    reponse = requests.get('https://zenquotes.io/api/quotes/random')
    json_data = json.loads(reponse.text)
    quotes = json_data[0]['q']+"-"+json_data[0]['a']
    return(quotes)


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    
    print(f'{username}: {user_message}, ({channel})')

    if message.author==client.user:
        return

    if   user_message.lower()=='hello':
        await message.channel.send(f"hello! {username}")    
    elif user_message.lower()=='bye':

         await message.channel.send(f"bye see you again {username}")
    elif any(word in user_message for word in sad_words):
        await message.channel.send(random.choice(encoraging_words))
    elif user_message.startswith('!joke'):
         await message.channel.send(random.choice(jokes))
    elif any(word in user_message for word in joke_words):
        await message.channel.send(random.choice(jokes))
    elif user_message.startswith('!help'):
        await message.channel.send('Commands\n!joke : for jokes\n!Myname : for show your name\n!quotes : for get random quotes') 
    
    elif user_message.startswith('!Myname'):
        await message.channel.send(f'Your name is {username}') 
    
    elif user_message.startswith('!quotes'):
        quote=get_quote()
        await message.channel.send(quote) 
    
keep_alive()
client.run(Token)
