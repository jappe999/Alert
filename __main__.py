#!/usr/bin/env python3

from watching import WatchDog

def main():
    dog = WatchDog()

    # Insert an array with one or more dictionaries
    dog.set_alert([
            {
                "time":5400,
                "text":"Isn't it time to take a break?",
                "subtext":"It's been 1.5 hours..."
            },
            {
                "time":5,
                "text":"Isn't it time to take a break?",
                "subtext":"It's been 1.5 hours..."
            }
        ])

    # Watch it.. :P
    dog.watch()

if __name__ == '__main__':
    main()
