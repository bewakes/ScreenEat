#!/usr/bin/env python3

from gi.repository import Gdk
import time
import re

# own exception class
class ManualError(Exception):
    def __init__(self, args):
        self.args = args
    
    def display(self):
        print(''.join(self.args))

"""
Simple screen shot class
TakeShot : returns a pixel buffer
SaveShot : accepts pixelbuffer and filename 
"""
class Screenshot(object):
    def __init__(self):
        # active window param
        self.screen = Gdk.Screen.get_default()
        self.active_window = self.screen.get_active_window()
        self.xactive, self.yactive, self.active_width, self.active_height = self.active_window.get_geometry()
        # whole window
        self.root_window = Gdk.get_default_root_window()
        self.x, self.y, self.full_width, self.full_height = self.root_window.get_geometry()

    def TakeShot(self, x,y, width, height, window):
        pixel_buffer = Gdk.pixbuf_get_from_window(window, x, y, width, height)
        return pixel_buffer

    def SaveShot(self, pixel_buffer, filename):
        # if no filename, create it using timestamp
        if not filename:
            filename = re.sub(r'\.', '', str(time.time()))
        try:
            if not pixel_buffer:
                raise ManualError("no pixel buffer. please take screenshot at first")
            else:
                pixel_buffer.savev(str(filename) + ".jpg", "jpeg", (), ())
        except ManualError as err:
            err.display()
            return False
        return True


def main():
    shot = Screenshot()
    # if full window
    #pb = shot.TakeShot(0, 0, shot.full_width, shot.full_height, shot.root_window)
    # if full active window
    pb = shot.TakeShot(0,0, shot.active_width, shot.active_height, shot.active_window)
    shot.SaveShot(pb, "test")

if __name__=="__main__":
    main()