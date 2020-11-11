import time
import os
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# global declarations
global log_area, input_file, output_file, experiment_menu


###################################
# function to return current time
###################################
def timestamp():
    return time.strftime('%x %X')


#############################
# function to close window
#############################
def quit_app():
    print('quit')
    root.destroy()


###################################################################
# called to convert the input experiment .txt file to .csv file
###################################################################
def convert_experiment():
    global experiment_menu
    if experiment_menu.current() == 0:  # check selected experiment
        if os.path.isfile('experiment_1.txt'):  # check file exists
            with open("experiment_1.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : experiment file converted to csv\n" % timestamp())
        else:
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : input file could not be found\n" % timestamp())
    elif experiment_menu.current() == 1:  # check selected experiment
        if os.path.isfile('experiment_2.txt'):  # check file exists
            with open("experiment_2.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : experiment file converted to csv\n" % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR] %s : input file could not be found\n" % timestamp())
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : input file could not be found\n" % timestamp())


##################################################
# called to display the log file in the log window
##################################################
def open_log():
    with open("log_file.txt", 'r') as file:
        log_area.insert(tk.END, '\n\n===Log File Start===\n\n')
        for line in file:
            log_area.insert(tk.END, line)
        log_area.insert(tk.END, '\n\n===Log File End===\n\n')
    log_area.see(tk.END)


##################################################
# called to create all widgets in the GUI
##################################################
def widgets():
    # menu
    menubar = tk.Menu()
    dropdown = tk.Menu(menubar, tearoff=0)
    dropdown.add_command(label="View Log", command=open_log)
    dropdown.add_command(label="Quit", command=quit_app)
    menubar.add_cascade(label="File", menu=dropdown)
    root.config(menu=menubar)

    # left_frame top
    left_frame = tk.Frame(root, bg='#e6e6e6')
    left_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ne')

    # left_frame bottom
    left_frame1 = tk.Frame(root, bg='#e6e6e6')
    left_frame1.grid(column=0, row=1, padx=5, pady=5, sticky='se')

    # right_frame
    right_frame = tk.Frame(root, bg='red')
    right_frame.grid(column=1, row=0, sticky='w')
    testButton = tk.Button(right_frame, text='Test', command=lambda: print('test'))
    testButton.grid(column=0, row=0)

    #####################################################
    # left_frame top widgets

    # input experiment file
    input_label = tk.Label(left_frame, text='Input File Text (.txt)')
    input_label.grid(column=0, row=1, sticky='ew')
    global input_file
    input_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=40, height=7,
                                           font='Calibri, 10', bg='black', fg='white')
    input_file.grid(column=1, row=1, padx=10, pady=10, columnspan=2)

    # output csv file
    output_label = tk.Label(left_frame, text='Output File Text (.csv)')
    output_label.grid(column=0, row=2, sticky='ew')
    global output_file
    output_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=40, height=7,
                                            font='Calibri, 10', bg='black', fg='white')
    output_file.grid(column=1, row=2, padx=10, pady=10, columnspan=2)

    experiment_label = tk.Label(left_frame, text='Choose Experiment')
    n = tk.StringVar()
    global experiment_menu
    experiment_menu = ttk.Combobox(left_frame, textvariable=n)
    experiment_menu['values'] = ('Experiment 1',
                                 'Experiment 2',
                                 'Experiment 3')
    experiment_button = tk.Button(left_frame, text="Convert", command=convert_experiment)
    experiment_menu.current(1)

    # left_frame grid placements
    experiment_label.grid(column=0, row=0, padx=10, pady=10, sticky='ew')
    experiment_menu.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
    experiment_button.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

    # left_frame bottom widgets

    global log_area
    log_area = scrolledtext.ScrolledText(left_frame1, wrap=tk.WORD, width=40, height=10,
                                         font=('Calibri', 12), bg='black', fg='white')
    log_label = tk.Label(left_frame1, text='Log output')

    log_label.grid(column=0, row=1, sticky='ew')
    log_area.grid(column=1, row=1, padx=10, pady=10, columnspan=2)

    # log
    with open("log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : widgets created\n" % timestamp())


def main():
    if os.path.exists("log_file.txt"):
        os.remove("log_file.txt")
    else:
        print("The file does not exist")
    print('main')

    root.title('Project')
    root.resizable(width=False, height=False)
    root.config(bg='grey')
    widgets()
    with open("log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window created.\n" % timestamp())


if __name__ == '__main__':
    print('start\n')
    root = tk.Tk()
    main()
    log_area.insert(tk.END, "[INFO]: window created.\n")
    root.mainloop()
    print('end\n')
