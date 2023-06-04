import io
import time
import aiohttp
import asyncio
import discord
import requests
import random
from random import choice
import time
from discord.ext import commands
import RPi.GPIO as GPIO
import socket

hostname = socket.gethostname()

client = discord.Client()
bot = commands.Bot(command_prefix='?')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = {
  "green":27,
  "yellow":5,
  "red":13,
  "buzzer":21
  }

for key in pins:
    value = pins.get(key)
    GPIO.setup(value,GPIO.OUT)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(' --- Ready! --- ')

@bot.command(pass_context=True)
async def blip(ctx, arg):
    print('blip ('+arg+') by:')
    print(ctx.message.author)

    for x in range(0, int(arg)):
        random_index = random.randint(0, len(pins) - 1)
        random_pin = choice(list(pins.values()))
        random_time = round(random.uniform(0.1,1.1), 2)

        GPIO.output(random_pin,GPIO.HIGH)
        time.sleep(random_time)
        GPIO.output(random_pin,GPIO.LOW)
        time.sleep(0.2)
    
    await ctx.send("Okay, I blip'ed "+hostname+" LED's "+str(arg)+" times!")

@bot.command(pass_context=True)
async def rainbow(ctx, arg):
    print('rainbow ('+arg+') by:')
    print(ctx.message.author)

    if (arg.isdigit()):
        for n in range(0, int(arg)):
            GPIO.output(pins["green"],GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pins["yellow"],GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pins["red"],GPIO.HIGH)
            time.sleep(0.2)

            GPIO.output(pins["green"],GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pins["yellow"],GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pins["red"],GPIO.LOW)
            time.sleep(0.2)

            GPIO.output(pins["red"],GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pins["yellow"],GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pins["green"],GPIO.HIGH)
            time.sleep(0.2)

            GPIO.output(pins["red"],GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pins["yellow"],GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pins["green"],GPIO.LOW)

            await ctx.send(str(n)+" rainbows")
    else:
        await ctx.send("Usage: ?rainbow <number>")
        
@bot.command(pass_context=True)
async def morsepi(ctx, *, arg):
    print('morsepi ('+arg+') by:')
    print(ctx.message.author)

    ref = {' ': ' ', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.', 
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '_': '..--.-'}

    for char in arg:
        for symbol in ref[char.upper()]:
            if symbol == ".":
                await ctx.send(" .")
                GPIO.output(pins["buzzer"],GPIO.HIGH)
                GPIO.output(pins["red"],GPIO.HIGH)
                time.sleep(0.2)

                GPIO.output(pins["buzzer"],GPIO.LOW)
                GPIO.output(pins["red"],GPIO.LOW)
                time.sleep(0.2)

            elif symbol == "-":
                await ctx.send(" -")
                GPIO.output(pins["buzzer"],GPIO.HIGH)
                GPIO.output(pins["red"],GPIO.HIGH)
                time.sleep(0.6)

                GPIO.output(pins["buzzer"],GPIO.LOW)
                GPIO.output(pins["red"],GPIO.LOW)
                time.sleep(0.6)

            else:
                time.sleep(0.5)
    await ctx.send(arg+" sent to "+hostname+" via morse code.")
@bot.command(pass_context=True)
async def alert(ctx):
    print('alert by:')
    print(ctx.message.author)

    GPIO.output(pins["buzzer"],GPIO.HIGH)
    GPIO.output(pins["red"],GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pins["buzzer"],GPIO.LOW)
    GPIO.output(pins["red"],GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(pins["buzzer"],GPIO.HIGH)
    GPIO.output(pins["red"],GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pins["buzzer"],GPIO.LOW)
    GPIO.output(pins["red"],GPIO.LOW)
    
    await ctx.send("Alerted "+hostname+"!")

bot.run("zzz")
