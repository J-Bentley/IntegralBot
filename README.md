# IntegralBot
A Discord bot running on a raspberrypi 3 that pulls data from free API's that is convenient to Drone pilots and gamers, also provides Discord commands to make LED's flash on a Raspberry Pi server.
# Setup
* [Discord.py](https://github.com/Rapptz/discord.py) & [Discord bot setup TL;DR](https://www.reddit.com/r/discordapp/comments/5tl7xd/how_to_make_a_discord_bot_tldr_edition/)
* [Basic RPi LED wiring example](https://imgur.com/a/dwl7CFP)
* Ensure pin channels are set on line 32 of this script; [RPi3 GPIO broadcomm layout reference](https://imgur.com/a/7G1IacE)
* Free API key & account for weather with [pyOWM](https://github.com/csparpa/pyowm). [Location lookup tool](https://openweathermap.org/).  
# Commands
* Weather: Shows wind, rain, snow, temperature, humidity data and weather status of set location (Angus, ON).
* Sun: Shows approx sunSET of today and predicts tomorrows sunRISE based of off that day's.
* Owstats: Shows overwatch stats for given battletag usage: ?owstats username-1234 (replace # with - in the battletag)
* alert: Turns on specific pins that are hooked up to a buzzer and red LED.
* blip: Flashes random GPIO pins (LED/buzzer) with random intervals.
* rainbow: Flashes a rainbow for given amount of times
* morsepi: converts sentence given to morse and flashes specific pins on server RPi. [Timings via](https://morsecode.scphillips.com/timing.html)

# TODO
* tee STDOUT to console & text file
* arg error handling
* program exit error handling (raw input?)
* fix owstats ?
