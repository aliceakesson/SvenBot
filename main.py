import discord
import os
import random

prefix = "woof"

commands = ["hello", "woof", "status", "howgay"]
commandDescribtions = ["Greet me!", 
                      "Bark at me, I dare you", 
                      "Economic balance of the human", 
                      "Try it"]

client = discord.Client()

@client.event
async def on_ready():
    print("Client: {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix) and len(message.content) > len(prefix) and message.content[len(prefix)] == " ": 
      #checks if its the prefix followed by something else
      #also (space in between)
      
      actualMessage = message.content[len(prefix) + 1:]

      index = 0
      for x in actualMessage:
        if x == " ":
          index+=1
        else:
          break

      messageClone = actualMessage[index:].lower() 
      #removes unneccesary spaces
      #right after the prefix and makes the message lowercase
      
      if messageClone.startswith("hello"):
        if len(messageClone) > 5 and messageClone[5:] != " ":
          return
        
        await message.channel.send("Hello!")
      
      elif messageClone.startswith("woof"):
        amountOfWords = len(message.content.split())
        correctMessage = "woof"

        for x in range(amountOfWords-1):
          correctMessage += " woof"

        if message.content.lower() == correctMessage:
          await message.channel.send(message.content)
      elif messageClone.startswith("status"):
        if len(messageClone) > 6 and messageClone[6:] != " ":
          return
        
        amountOfMoney = 0
        
        await message.channel.send("__**" + str(message.author.name)+ "'s status:**__" ""+ "\nMoney: " + str(amountOfMoney) + " coins")

      elif messageClone.startswith("howgay"):
        if len(messageClone) > 6 and messageClone[6:] != " ":
          return

        await message.channel.send(str(message.author.name) + " is " + str(random.randint(0, 100)) + "% gay")

      elif messageClone.startswith("help"):
        if len(messageClone) > 4 and messageClone[4:] != " ":
          return

        messageToSend = ""
        for x in range(len(commands)):
          messageToSend += "**woof " + commands[x] + "**: " + commandDescribtions[x] + "\n\n"
        
        await message.channel.send(messageToSend)


client.run(os.getenv("TOKEN"))
