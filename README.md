# IntegralBot
Discord bot running on raspberr ypi with ability to turn on LED's via discord commands.

# Setup
* [Discord.py](https://github.com/Rapptz/discord.py) & [Discord bot setup TL;DR](https://www.reddit.com/r/discordapp/comments/5tl7xd/how_to_make_a_discord_bot_tldr_edition/)
* [Basic RPi LED wiring example](https://imgur.com/a/dwl7CFP)
* Ensure pin channels are set on line 32 of this script; [RPi3 GPIO broadcomm layout reference](https://imgur.com/a/7G1IacE)

# Commands
* alert: Turns on specific pins that are hooked up to a buzzer and red LED.
* blip: Flashes random GPIO pins (LED/buzzer) with random intervals.
* rainbow: Flashes a rainbow for given amount of times
* morsepi: converts sentence given to morse and flashes specific pins on server RPi. [Timings via](https://morsecode.scphillips.com/timing.html)

