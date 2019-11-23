import io
import time
import aiohttp
import asyncio
import discord
import pyowm
import requests
import random
from random import choice
import time
from discord.ext import commands
import RPi.GPIO as GPIO
import socket

hostname = socket.gethostname()

weather_location = 'xxx'
owm = pyowm.OWM('yyy')

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
    print('---- Ready! ----')

@bot.command(pass_context=True)
async def weather(ctx):
    print('weather by:')
    print(ctx.message.author)

    observation = owm.weather_at_place(weather_location)
    w = observation.get_weather()

    weather_icon = w.get_weather_icon_url() 
    wind = w.get_wind()
    humidity = w.get_humidity()  
    temp = w.get_temperature('celsius')
    status = w.get_detailed_status()
    rain = w.get_rain()
    snow = w.get_snow()

    async with aiohttp.ClientSession() as session:
        async with session.get(weather_icon) as resp:
            if resp.status != 200:
                return await ctx.send('Error grabbing icon!')
                exit(1)
            data = io.BytesIO(await resp.read())

    weather_output = "Here's todays weather in {}!\nRain: {}\nSnow: {}\nWind: {}\nHumidity: {}\nTemp: {}\nStatus: {}\n".format(weather_location, rain, snow, wind, humidity, temp, status)
    await ctx.send(weather_output,file=discord.File(data, 'weather_image.png'))

@bot.command(pass_context=True)
async def sun(ctx):
    print('sunset by:')
    print(ctx.message.author)

    observation = owm.weather_at_place(weather_location)
    w = observation.get_weather()

    sunset_time = w.get_sunset_time('iso')
    sunrise_time = w.get_sunrise_time('iso')

    sunset_output = "The sun sets upon {} at {} and rises tomorrow around {}.".format(weather_location, sunset_time, sunrise_time)
    await ctx.send(sunset_output)

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
        #await ctx.send("Pin "+str(random_pin)+" blip'd for "+str(random_time))
    
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

@bot.command(pass_context=True)
async def owstats(ctx, arg):
    print('owstats by:')
    print(ctx.message.author)

    if "#" in arg:
    	await ctx.send("Thats a spooky symbol, replace it with this -")

    try:
        stats = requests.get('https://ow-api.com/v1/stats/pc/us/'+arg+'/profile').text.replace(":"," ")
    except:
        await ctx.send("Error communicating with Overwatch stats API!")

    nameindex = stats.find("name")
    statsname = stats[nameindex+6 : nameindex+22]

    levelindex = stats.find("level")
    statslevel = stats[levelindex+7 : levelindex+9]

    prestigeindex = stats.find("prestige")
    statsprestige = stats[prestigeindex+10 : prestigeindex+11]

    gamesindex = stats.find("played")
    statsgames = stats[gamesindex+8 : gamesindex+11]

    wonindex = stats.find("won")
    statswon = stats[wonindex+5 : wonindex+9]

    cardindex = stats.find("cards")
    statscard = stats[cardindex+6 : cardindex+9]

    message = ("Name: "+ statsname+"\n"+"Level: "+statslevel+"\n"+"Prestige: "+statsprestige+"\n"+"Games played: "+statsgames+"\n"+"Games won: "+statswon+"\n"+"Cards: "+statscard)
    await ctx.send(message)

bot.run("zzz")
