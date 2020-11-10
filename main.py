import time
import tkinter as tk
from tkinter import scrolledtext

global text_area


def timestamp():
    return time.strftime('%x %X')


def quit_app():
    print('quit')
    root.destroy()


def open_log():
    with open("log_file.txt", 'r') as file:
        if file.closed:
            print("[ERROR]: Log file is closed.\n")
            text_area.insert(tk.END, "[ERROR]: Log file is closed.\n")
        else:
            try:
                for line in file:
                    text_area.insert(tk.END, '\n\n===Log File Start===\n\n')
                    text_area.insert(tk.END, line)
                    text_area.insert(tk.END, '\n\n===Log File End===\n\n')
                    text_area.see(tk.END)
            except:
                print("[ERROR]: Log file is closed.\n")
                text_area.insert(tk.END, "[ERROR]: Log file is closed.\n")


def widgets():
    # menu
    menubar = tk.Menu(root)
    dropdown = tk.Menu(menubar, tearoff=0)
    dropdown.add_command(label="Open Log", command=open_log)
    dropdown.add_command(label="Quit", command=quit_app)
    menubar.add_cascade(label="File", menu=dropdown)
    root.config(menu=menubar)

    # elements
    label1 = tk.Label(root, text='Quit and close')

    button1 = tk.Button(text='Quit', command=quit_app)

    global text_area
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10,
                                          font=("Calibri", 12), bg="black", fg="white")

    label1.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    button1.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

    text_area.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
    text_area.focus()


def window_geometry():
    # window geometry
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    window_width = int((screen_width / 1.5) + 50)
    window_height = int(screen_height / 1.5)
    window_x_pos = int(screen_width / 8)
    window_y_pos = int(screen_height / 8)

    print("screen height: " + str(screen_height))
    print("screen width: " + str(screen_width))
    print("window height: " + str(window_height))
    print("window width: " + str(window_width))
    root_geometry = str(window_width) + 'x' + str(window_height) + \
        '+' + str(window_x_pos) + '+' + str(window_y_pos)
    root.geometry(root_geometry)


def main():
    print('main')

    root.title('Project')
    root.resizable(width=False, height=False)
    root.config(bg='grey')
    window_geometry()
    widgets()


if __name__ == '__main__':
    print('start\n')
    root = tk.Tk()
    main()
    text_area.insert(tk.END, "Log[INFO]: window created\n")
    with open("log_file.txt", 'w') as log_file:
        log_file.write("[INFO] %s : window created\n" % timestamp())
    root.mainloop()
    print('end\n')
