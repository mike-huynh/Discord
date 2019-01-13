import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "$")

class function:
    def __init__(self):
        self.acc = 0
        pass

    #Resets the accum
    def reset(self):
        self.acc = 0
        return "Accumulator has been reset"

    #Sets the accum to your preference
    def setAcc(self, x):
        self.acc = int(x)
        return "Accumulator has been set to " + x

    # Returns the accumulator number
    def display(self):
        return self.acc

    #Adds numbers to the accumulator
    def add(self, lst):
        for x in lst:
            self.acc += int(x)
        return self.acc

    #Subtracts from the accumulator
    def sub(self, lst):
        for x in lst:
            self.acc -= int(x)
        return self.acc

    #Multiplies the accumulator
    def mult(self, lst):
        if self.acc == 0:
            self.acc = 1
        else:
            pass
        for x in lst:
            self.acc *= int(x)
        return self.acc

f = function()

@client.event
async def on_ready():
    print("Bot is connected.")

@client.event
async def on_message(message):
    if message.content.upper() == "COOKIE":
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper() == "BOMB":
        await client.send_message(message.channel, ":bomb:")

    if message.content.upper() == "POTATO":
        await client.send_message(message.channel, ":potato:")
        
    if message.content.upper() == "THINKING EMOJI":
        await client.send_message(message.channel, ":thinking:")

    if message.content.upper() == "NO":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> does not know de wey." % (userID))
        
    if message.content.upper().startswith('+U'):
        userID = message.author.id
        msg = message.content.split(" ")
        await client.send_message(message.channel, "Do you know %s" % (" ".join(msg[1:])))
        
    if message.content.upper().startswith('+F'):
        userID = message.author.id
        msg = message.content.split(" ")
        await client.send_message(message.channel, "<@%s> has paid their respects to %s" % (userID, " ".join(msg[1:])))
        
    if message.content.upper() == "!F":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> has paid their respects." % (userID))

    if message.content.upper().startswith('ADD'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.add(msg[1:])))

    if message.content.upper().startswith('SUB'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.sub(msg[1:])))

    if message.content.upper().startswith('MULT'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.mult(msg[1:])))

    if message.content.upper().startswith('SET TO'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.setAcc(msg[2])))

    if message.content.upper().startswith('RESET'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.reset()))

    if message.content.upper().startswith('DISPLAY'):
        msg = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (f.display()))

client.run("NDQ2NzA0OTkyNjQwOTU4NDY1.Dd88Dw.1U3h2kKIIpkAP9YJe29_88sdKsM")

