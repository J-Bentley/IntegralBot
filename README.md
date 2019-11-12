# IntegralBot
A Discord bot running on a raspberrypi 3 that pulls data from free API's that convenient to Drone pilots and gamers, as well as provides user output to the server via Discord commands to GPIO pins hooked up to LED's & a buzzer.
# Setup
* [Discord.py](https://github.com/Rapptz/discord.py)
* [Basic RPi LED wiring example](https://imgur.com/a/dwl7CFP)
* Ensure pins are set on line 32 [RPi3 GPIO broadcomm layout reference](https://imgur.com/a/7G1IacE)
* Free API key & account with for weather [pyOWM](https://github.com/csparpa/pyowm). 
* [Location lookup tool.](https://openweathermap.org/) 
# Commands
* Weather: Shows wind, rain, snow, temperature, humidity data and weather status of set location.
* Sun: Shows approx sunSET of today and predicts tomorrows sunRISE based of off "todays'".
* Owstats: Shows overwatch stats for given battletag usage: ?owstats username-1234 (replace # with -, in the battletag)
* alert: Turns on specific pins set in pins dictionary that are hooke dup to a buzzer and red LED.
* blip: Flashes random GPIO pins (LED/buzzer) for random amounts of time.
# TODO
* tee STDOUT to console & text file
* arg error handling
* program exit error handling (raw input?)
* Morsepi command
* fix owstats ?
