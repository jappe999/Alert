#!/usr/bin/env python3

import time, pyautogui, sys
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GObject
except ImportError as e:
    print('We encounterd an error:\n', e)
from threading import Thread
from subprocess import Popen

GObject.threads_init()

class WatchDog(object):
    def __init__(self, notif='gtk'):
        self.time_start = time.time()
        self.dogs = []
        self.mouse_position = pyautogui.position()
        self.mouse_timeout = 0
        self.notif = notif # Type of notifier (gtk or notify-send)

    def reset_time(self):
        self.time_start = time.time()

    def get_time(self, time):
        return self.time_start + time

    def active(self):
        # If the mouse has not moved
        if self.mouse_position == pyautogui.position():
            return False
        return True

    def set_alert(self, dogs):
        # Add the array to the class' object
        for dog in dogs:
            dog['is_alerted'] = False
            dog['time'] += self.time_start # Convert to unix time
            self.dogs.append(dog)

    def alert(self, text, subtext=''):
        if self.notif == 'gtk':
            # Display dialog
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                        Gtk.ButtonsType.OK, text)
            dialog.format_secondary_text(subtext)
            dialog.run()

            # Close dailog and update GUI
            dialog.destroy()
            while Gtk.events_pending():
                Gtk.main_iteration()

            print('INFO dialog closed')

        elif self.notif == 'notify-send':
            Popen(['notify-send', text, subtext])

    def watch(self):
        t = Thread(target=self._watch)
        t.start()

    # The actual watch function
    def _watch(self):
        while True:
            if self.active(): # If mouse has moved
                self.mouse_timeout = 0
            elif self.mouse_timeout >= 900: # 15 minutes strike
                self.reset_time()
                print('Resetting...')
                continue

            self.mouse_timeout += 1
            if len(self.dogs) > 0:
                for dog in self.dogs:
                    if time.time() >= dog['time'] and dog['is_alerted'] == False:
                        t = Thread(target=self.alert, args=(dog['text'], dog['subtext'],))
                        t.start()
                        dog['is_alerted'] = True
                        self.dogs.remove(dog)
            else:
                self.alert('No more dogs', 'There are no more dogs...')
                self.alert('Maybe it\'s time to stop?')
                print('Exiting...')
                sys.exit(0)
            time.sleep(1)

if __name__ == '__main__':
    test_dog = WatchDog('notify-send')
    test_dog.set_alert([
            {
                "time":1,
                "text":"Isn't it time to take a break?",
                "subtext":"It's been 5 seconds..."
            }
        ])
    test_dog.watch()
