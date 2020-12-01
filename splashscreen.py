# --------------------------------------------------------------
# ET4244 Outcome Based Laboratory 2: Autumn Semester 2020
# File name   : splashscreen.py
# Created by  : Damian Larkin
# Last update : 1st December 2020
# --------------------------------------------------------------
# Overview: Splash screen for main project window
# --------------------------------------------------------------

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import tkinter as tk


def splash_window():

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    width = 525
    height = 315
    x = w/2 - width/2
    y = h/2 - height/2

    splash.geometry('%dx%d+%d+%d' % (width, height, x, y))
    splash.overrideredirect(1)
    splash.configure(bg='black')

    label1 = tk.Label(splash, text='Test', font='calibri 16', bg='black', fg='white')
    label1.grid(column=0, row=0, padx=10, pady=10, sticky='ew')


# --------------------------------------------------------------
# Module is only run as a script or with python -m,  but not
# when it is imported.
# --------------------------------------------------------------
if __name__ == '__main__':
    print('program start')

    root = tk.Tk()

    splash = tk.Toplevel()
    splash.attributes('-topmost', True)
    splash_window()
    splash.after(3000, splash.destroy)

    root.mainloop()

    print('program end')
