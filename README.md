# Brewpost

## A Tilt Hydrometer Reading Utility  

Brewpost is a simple ~~utility~~ hack that wraps the great work done by Simon Bowler, who wrote the [Tilt Hydrometer Tilt Polling library.](https://github.com/sibowler/brewpi-brewometer)  

This code takes the data polled from the [Tilt Hydrometer](https://tilthydrometer.com/products/brewometer) Sensor and sends the data to a specific URL.

In my case I'm posting this to a private google sheet that tracks the specific gravity of my beer over time.

The url file is missing from this project, you'll have to provide your own if you intend to use this.

The `beerinprogress` file is the name of the actual beer that is fermenting.

The brewpost.py file is hardcoded to scan for a Red sensor.

The cron file is named `brewpost` and is also hard coded to use paths under the /home/ directory for a user named brewpost.