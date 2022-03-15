import discord
import os

prefix = "woof"

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


client.run(os.getenv("TOKEN"))
