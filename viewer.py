'''
Created on Jul 28, 2016

@author: Vladimir

@description: Скрипт для просмотра изображений
'''

from itertools import cycle

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class Viewer(tk.Tk):
    def __init__(self, image_files, x=100, y=100, delay=3000):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image) for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()
