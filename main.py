import discord
import os
import random
import requests
import json
from keep_alive import keep_alive

prefix = "woof"

commands = ["hello", "woof", "status", "howgay", "randomdog"]
commandDescribtions = [
    "Greet me!", 
    "Bark at me, I dare you", 
    "Economic balance of the human",
    "Try it",
    "Dogs"
]

client = discord.Client()

def get_random_dog():
  response = requests.get("https://random.dog/api/woof")
  json_data = json.loads(response.image) #response.iomage??

@client.event
async def on_ready():
    print("Client: {0.user}".format(client))


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

          get_random_dog()


keep_alive()
client.run(os.getenv("TOKEN"))
