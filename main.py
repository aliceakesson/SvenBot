import discord
import os
import random
import requests
import json
from replit import db
from keep_alive import keep_alive

prefix = "!"

commands = ["hello", "woof", "bal", "howgay", "dog", "bark", "beg", "8ball"]
commandDescribtions = [
    "Greet me!", "Bark at me, I dare you", "Economic balance of the human",
    "Try it", "Dog.", "I bark at you.",
    "Hm. I guess you can ask me for some money", "Test my wisdom"
]

moneyDatabase = "money"

client = discord.Client()


def get_random_dog():
    response = requests.get("https://random.dog/woof.json")
    json_data = json.loads(response.text)

    return (json_data['url'])


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(prefix + "help"))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix) and len(
            message.content) > len(prefix):
        #checks if its the prefix followed by something else

        actualMessage = message.content[len(prefix):]

        index = 0
        for x in actualMessage:
            if x == " ":
                index += 1
            else:
                break

        messageClone = actualMessage[index:].lower()
        #removes unneccesary spaces
        #right after the prefix and makes the message lowercase

        #pref + hello
        if messageClone.startswith("hello"):
            if len(messageClone) > 5 and messageClone[5:] != " ":
                return

            greetings = ["Hello", "Greetings", "What's up"]

            noGreetingPossibility = random.randint(0, 1000)

            if noGreetingPossibility == 0:
                await message.channel.send("No greeting for you")

            else:
                await message.channel.send(
                    greetings[random.randint(0,
                                             len(greetings) - 1)] + " " +
                    "<@" + str(message.author.id) + ">" + "!")

        #woof woof
        elif messageClone.startswith("woof"):
            amountOfWords = len(messageClone.split())

            correctMessage = ""
            if prefix == "woof" or prefix == "woof ":
                correctMessage = "woof "

            for x in range(amountOfWords):
                correctMessage += "woof "

            correctMessage = correctMessage[0:len(correctMessage) - 1]

            if messageClone.lower() == correctMessage:
                await message.channel.send(message.content[len(prefix):])

        #woof bal
        elif messageClone.startswith("bal"):
          if len(messageClone) > 3 and messageClone[3:] != " ":
              return

          amountOfMoney = 0

          if str(message.author.id) in db.keys():
            amountOfMoney = db[str(message.author.id)][moneyDatabase]

          await message.channel.send("<@" + str(message.author.id) + ">" +
                                     "'s balance:"
                                     "" + "\nMoney: " + str(amountOfMoney) +
                                     " coins")

        #woof howgay
        elif messageClone.startswith("howgay"):
            if len(messageClone) > 6 and messageClone[6:7] != " ":
                return

            wordAlt = ["gay", "homosexual", "playing for the other team"]

            person = str(message.author.id)
            if len(messageClone) > 8 and messageClone[7:9] == "<@" and messageClone[len(messageClone)-1:] == ">":

              person = messageClone[9:len(messageClone)-1]
              
            await message.channel.send(
                "<@" + person + ">" + " is " +
                str(random.randint(0, 100)) + "% " +
                wordAlt[random.randint(0,
                                       len(wordAlt) - 1)])

        #woof help
        elif messageClone.startswith("help"):
            if len(messageClone) > 4 and messageClone[4:] != " ":
                return

            messageToSend = ""
            for x in range(len(commands)):
                messageToSend += "**" + prefix + commands[
                    x] + "**: " + commandDescribtions[x] + "\n\n"

            await message.channel.send(messageToSend)

        #woof randomdog
        elif messageClone.startswith("dog"):
            if len(messageClone) > 9 and messageClone[9:] != " ":
                return

            image = get_random_dog()
            await message.channel.send(image)

        #woof barkatme
        elif messageClone.startswith("bark"):
            if len(messageClone) > 8 and messageClone[8:] != " ":
                return

            possibleBarks = ["bark", "grr", "woof", "growl"]

            finalBark = ""

            for x in range(random.randint(5, 10)):
                word = possibleBarks[random.randint(0, len(possibleBarks) - 1)]

                for y in range(len(word)):
                    amountOfCharacters = random.randint(1, 3)

                    for z in range(amountOfCharacters):
                        upperOrLowercase = random.randint(0, 1)

                        if upperOrLowercase == 0:
                            finalBark += word[y].lower()
                        else:
                            finalBark += word[y].upper()

                finalBark += " "

            await message.channel.send(finalBark)

        #beg
        elif messageClone.startswith("beg"):
          if len(messageClone) > 3 and messageClone[3:] != " ":
              return
            
          # del db[str(message.author.id)]
            
          money = random.randint(1, 30) * 10
          moneyRightNow = money
          
          if str(message.author.id) in db.keys():
            moneyRightNow = int(db[str(message.author.id)][moneyDatabase]) + money
            db[str(message.author.id)][moneyDatabase] = moneyRightNow
          else:
            db[str(message.author.id)] = {moneyDatabase: money}

          await message.channel.send("You earnt " + str(money) + " coins" + "\nCurrent balance: " + str(moneyRightNow) + " coins")
         
        #8ball
        elif messageClone.startswith("8ball"):
            if len(messageClone) > 5 and messageClone[5] != " ":
                return

            amountOfWords = len(messageClone.split())
            if amountOfWords == 1:

                wordAlt = [
                    "You need to ask me something",
                    "I can't seem to find the question",
                    "Dude you can't just ask me to answer without a question"
                ]

                await message.channel.send(wordAlt[random.randint(
                    0,
                    len(wordAlt) - 1)])
                return

            wordAlt = [
                "I guess, why not", "Yes", "No", "Hard pass",
                "I don't think so bro", "Sorry, but no", "Absolutely yes",
                "YES, suprised you're even asking", "Maybe, maybe..",
                "Do you really wanna know the answer", "Ask again",
                "I'd rather die", "Please no", "You wish", "I don't care",
                "Sure ;)", "Don't count on it",
                "Sorry what was I supposed to answer", "Doubtful",
                "Very likely", "What do you think the answer is",
                "You're a moron for asking", "Hell no", "I hope not",
                "I hope so", "I suppose so", ""
            ]

            await message.channel.send(wordAlt[random.randint(
                0,
                len(wordAlt) - 1)])


        elif messageClone.startswith("gamble"):
          if len(messageClone) > 6 and messageClone[6:] != " ":
            return

          moneyRightNow = 0
          if str(message.author.id) in db.keys():
            moneyRightNow = int(db[str(message.author.id)][moneyDatabase]) 

          else:
            db[str(message.author.id)] = {moneyDatabase: 0}

          moneyRequested = 0
          if(len(messageClone)) > 7:
            moneyRequested = messageClone[7:]
          else:
            return

          if " " in messageClone:
            messageClone = messageClone[0:messageClone.indexOf(" ")]

          print(messageClone)
          
keep_alive()
client.run(os.getenv("TOKEN"))
