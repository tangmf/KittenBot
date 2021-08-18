import discord
import json
import os
import random
from discord.ext import commands
from discord.ext import tasks
import discord,asyncio,os

client = commands.Bot(command_prefix = '.')
import threading

health = 100
happiness = 100
hunger = 100

print("The client is now setting up...")



@client.event
async def on_ready():
    print("Setup complete!")
    print(client.user.name)
    print(client.user.id)
    print(f'Ping: {round(client.latency * 1000)}ms')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'meow'))

def printdetails():
    global health
    global hunger
    print ("Health: " + str(health) + "\n" + "Hunger: " + str(hunger) + "\n" + "Happiness: " + str(happiness))


def tick():
  global hunger
  global health
  global happiness
  threading.Timer(60.0, tick).start()
  hunger = hunger - 5
  happiness = happiness - 2
  print ("tick activated")
  if hunger <= 0:
      hunger = 0
      health -= 5
      print("starving!")
  if happiness <= 0:
      happiness = 0
      health -= 10
  printdetails()
  
tick()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command')

@client.command()
async def feed(ctx):
    global hunger
    global happiness
    hunger = hunger + 10
    happiness = happiness + 2
    if hunger >= 100:
        hunger = 100
    if happiness >= 100:
        happiness = 100
    await ctx.send(f'Nom nom')
    print("Fed. Current hunger: " + hunger)

@client.command()
async def snuggle(ctx):
    global happiness
    happiness = happiness + 10
    if happiness >= 100:
        happiness = 100
    await ctx.send(f'Zzzz')
    print("Snuggled. Current happiness: " + happiness)

    
@client.command()
async def sleep(ctx):
    global happiness
    global health
    happiness = happiness + 5
    health = health + 10
    if happiness >= 100:
        happiness = 100
    if health >= 100:
        health = 100
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'Zzzz'))

@client.command()
async def wakeup(ctx):
    global health
    health = health + 5
    if health >= 100:
        health = 100
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'meow'))
    
@client.command()
async def ping(ctx):

    await ctx.channel.send(f'I am here!\nPing: {round(client.latency * 1000)}ms')
    
@client.command()
async def rename(ctx, name):
    print("Renamed to " + str(name))
    await client.user.edit(nick=name)
    
@client.command()
async def status(ctx):
    await ctx.send(f'{client.user.name}\nHealth : {health}\nHunger : {hunger}\nHappiness : {happiness} ')
        

client.run(<token here>)


