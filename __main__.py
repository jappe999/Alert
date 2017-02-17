#!/usr/bin/env python3

from watching import WatchDog

def main():
    dog = WatchDog('notify-send')

    # Insert an array with one or more dictionaries
    dog.set_alert([
            {
                "time":5400,
                "text":"Isn't it time to take a break?",
                "subtext":"It's been 1.5 hours..."
            },
            {
                "time":120,
                "text":"Hello World!",
                "subtext":"It's been 2 minutes since I booted..."
            },
            {
                "time":5,
                "text":"5 seconds test",
                "subtext":"I show up after 5 seconds..."
            }
        ])

    # Watch it.. :P
    dog.watch()

if __name__ == '__main__':
    main()
