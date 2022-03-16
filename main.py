import discord
import os
import random
import requests
import json
from keep_alive import keep_alive

prefix = "woof"

commands = ["hello", "woof", "status", "howgay", "randomdog", "barkatme"]
commandDescribtions = [
    "Greet me!", 
    "Bark at me, I dare you", 
    "Economic balance of the human",
    "Try it",
    "Dogs",
    "I bark at you."
]

client = discord.Client()

def get_random_dog():
  response = requests.get("https://random.dog/woof.json")
  json_data = json.loads(response.text)

  return (json_data['url'])
  
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game("woof help"))

  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix) and len(message.content) > len(
            prefix) and message.content[len(prefix)] == " ":
        #checks if its the prefix followed by something else
        #also (space in between)

        actualMessage = message.content[len(prefix) + 1:]

        index = 0
        for x in actualMessage:
            if x == " ":
                index += 1
            else:
                break

        messageClone = actualMessage[index:].lower()
        #removes unneccesary spaces
        #right after the prefix and makes the message lowercase

        #woof hello
        if messageClone.startswith("hello"):
            if len(messageClone) > 5 and messageClone[5:] != " ":
                return

            await message.channel.send("Hello!")

        #woof woof
        elif messageClone.startswith("woof"):
            amountOfWords = len(message.content.split())
            correctMessage = "woof"

            for x in range(amountOfWords - 1):
                correctMessage += " woof"

            if message.content.lower() == correctMessage:
                await message.channel.send(message.content)

        #woof status
        elif messageClone.startswith("status"):
            if len(messageClone) > 6 and messageClone[6:] != " ":
                return

            amountOfMoney = 0

            await message.channel.send("__**" + str(message.author.name) +
                                       "'s status:**__"
                                       "" + "\nMoney: " + str(amountOfMoney) +
                                       " coins")

        #woof howgay
        elif messageClone.startswith("howgay"):
            if len(messageClone) > 6 and messageClone[6:] != " ":
                return

            await message.channel.send(
                str(message.author.name) + " is " +
                str(random.randint(0, 100)) + "% gay")

        #woof help
        elif messageClone.startswith("help"):
            if len(messageClone) > 4 and messageClone[4:] != " ":
                return

            messageToSend = ""
            for x in range(len(commands)):
                messageToSend += "**woof " + commands[
                    x] + "**: " + commandDescribtions[x] + "\n\n"

            await message.channel.send(messageToSend)

        #woof randomdog 
        elif messageClone.startswith("randomdog"):
          if len(messageClone) > 9 and messageClone[9:] != " ":
                return

          image = get_random_dog()
          await message.channel.send(image)

        #woof barkatme
        elif messageClone.startswith("barkatme"):
          if len(messageClone) > 8 and messageClone[8:] != " ":
                return

          possibleBarks = ["bark", "grr", "woof", "growl"]

          finalBark = ""

          for x in range(5):
            word = possibleBarks[random.randint(0,len(possibleBarks)-1)]
            
            for y in range(len(word)):
              amountOfCharacters = random.randint(1,3)

              for z in range(amountOfCharacters):
                upperOrLowercase = random.randint(0,1)

                if upperOrLowercase == 0:
                  finalBark+=word[y].lower()
                else:
                  finalBark+=word[y].upper()

            finalBark+=" "

          await message.channel.send(finalBark)

keep_alive()
client.run(os.getenv("TOKEN"))
