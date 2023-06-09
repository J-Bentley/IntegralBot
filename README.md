# Morsepi
Discord bot running on raspberry pi that converts text to morse code via led/buzzer on gpio pins. Also some fun stuff.

# Setup
* [Discord.py](https://github.com/Rapptz/discord.py) & [Discord bot setup TL;DR](https://www.reddit.com/r/discordapp/comments/5tl7xd/how_to_make_a_discord_bot_tldr_edition/)
* [Basic RPi LED wiring example](https://imgur.com/a/dwl7CFP)
* Ensure pin channels are set on line 32; [GPIO broadcomm reference](https://imgur.com/a/7G1IacE)

# Commands
* morsepi: converts sentence given to morse code and flashes specific pins on server RPi. [Source.](https://morsecode.world/international/timing.html)
* alert: Turns on specific pins that are hooked up to a buzzer and red LED.
* blip: Flashes random GPIO pins with random intervals.
* rainbow: Flashes a rainbow for given amount of times

