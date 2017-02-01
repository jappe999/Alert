#!/usr/bin/env python3

import time, pyautogui, sys, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from threading import Thread

GObject.threads_init()

class WatchDog(object):
    def __init__(self):
        self.time_start = time.time()
        self.dogs = []
        self.mouse_position = pyautogui.position()
        self.mouse_timeout = 0

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

    def alert(self, text, subtext):
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

    def watch(self):
        t = Thread(target=self._watch)
        t.start()

    # The actual watch function
    def _watch(self):
        while True:
            if self.active(): # If mouse has moved
                self.mouse_timeout = 0
            elif self.mouse_timeout >= 4: # 15 minutes
                self.reset_time()
                continue

            self.mouse_timeout += 1

            if len(self.dogs) > 0:
                for dog in self.dogs:
                    if time.time() >= self.get_time(dog['time']) and dog['is_alerted'] == False:
                        t = Thread(target=self.alert, args=(dog['text'], dog['subtext'],))
                        t.start()
                        dog['is_alerted'] = True
            else:
                sys.exit(0)
            time.sleep(1)
