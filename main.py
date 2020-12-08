# ------------------------------------------------------------------
# File name       : main.py
# ------------------------------------------------------------------
# Group number    : 1
# Group members   : Damian Larkin (18230253) & James Cusack (18250416)
# Last updated on : 02/12/2020
# ------------------------------------------------------------------
# Module description:
#   python script to satisfy project requirements for ET4244 Autumn
#   semester. Converts experiment files to .csv and graphs the results
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Modules to import
# ------------------------------------------------------------------
import csv
import time
import os
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image
from PIL import ImageTk

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import conversion  # .txt to .csv conversion script

# global declarations
global log_area, input_file, output_file, experiment_menu, right_frame, graph_select, row_array, ax1, fig1, save_text, plot_flag
plot_flag = 0


# ------------------------------------------------------------------
# def create_graph()
# ------------------------------------------------------------------
# function to generate a graph using matplotlib
# ------------------------------------------------------------------
def create_graph():
    # print('plotting start')

    global row_array, ax1, fig1
    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = fig1.add_subplot(111)
    row_array = []
    if os.path.isfile('csv/output.csv'):
        with open('csv/output.csv', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in filereader:
                row_array.append(row)
        row_array = np.array(row_array, dtype=object)
        print([row_array[1][0]])

        x = np.array([])
        y = np.array([])
        global plot_flag
        plot_flag = 0
        if graph_select.current() == 0:
            log_area.insert(tk.END, '[WARN]: no graph type selected - graph aborted\n')
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[WARN] %s : no graph type selected - graph function stopped\n" % timestamp())
            log_area.see(tk.END)
            print('graph aborted - function stopped')
            return
        elif graph_select.current() == 1:
            # print([row_array[i][1]] + [row_array[i][2]])
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][1]], axis=None)
            ax1.set_title('Accelerometer X')
            ax1.set_ylabel('Accelerometer Value')
        elif graph_select.current() == 2:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][2]], axis=None)
            ax1.set_title('Accelerometer Y')
            ax1.set_ylabel('Accelerometer Value')
        elif graph_select.current() == 3:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][3]], axis=None)
            ax1.set_title('Accelerometer Z')
            ax1.set_ylabel('Accelerometer Value')
        elif graph_select.current() == 4:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][4]], axis=None)
            ax1.set_title('Temperature')
            ax1.set_ylabel('Temperature')
        elif graph_select.current() == 5:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][5]], axis=None)
            ax1.set_title('Gyroscope X')
            ax1.set_ylabel('Gyroscope Value')
        elif graph_select.current() == 6:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][6]], axis=None)
            ax1.set_title('Gyroscope Y')
            ax1.set_ylabel('Gyroscope Value')
        elif graph_select.current() == 7:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][7]], axis=None)
            ax1.set_title('Gyroscope Z')
            ax1.set_ylabel('Gyroscope')
        elif graph_select.current() == 8:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][8]], axis=None)
            ax1.set_title('Angle/Pitch')
            ax1.set_ylabel('Angle/Pitch Value')
        elif graph_select.current() == 9:
            for i in range(1, len(row_array)):
                x = np.append(x, [row_array[i][9]], axis=None)
            ax1.set_title('Roll')
            ax1.set_ylabel('Roll Value')

        for i in range(1, len(row_array)):
            y = np.append(y, [i], axis=None)

        ax1.plot(y.astype(float), x.astype(float))
        ax1.grid()
        ax1.set_xlabel('Sensor Value (1-240)')
        fig1.tight_layout()
        canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
        canvas1.draw()
        canvas1.get_tk_widget().grid(column=0, row=2, columnspan=5)
        plot_flag = 1

        print('plot complete - creating log entry')

    else:
        log_area.insert(tk.END, '[WARN]: \"csv/output.csv\" not found - plot aborted\n')
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[WARN] %s : \"csv/output.csv\" not found - plot aborted\n" % timestamp())


# ------------------------------------------------------------------
# def reset_app()
# ------------------------------------------------------------------
# function to reset all widgets
# ------------------------------------------------------------------
def reset_app():
    input_file.delete(1.0, tk.END)
    output_file.delete(1.0, tk.END)
    log_area.delete(1.0, tk.END)
    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = fig1.add_subplot(111)
    canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(column=0, row=2, columnspan=5)
    log_area.insert(tk.END, '[INFO]: window reset\n')
    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window reset\n" % timestamp())


# ------------------------------------------------------------------
# def clear_graph()
# ------------------------------------------------------------------
# function to clear the current graph area
# ------------------------------------------------------------------
def clear_graph():
    print('graph cleared')
    graph_select.current(0)
    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = fig1.add_subplot(111)
    canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(column=0, row=2, columnspan=5)
    global plot_flag
    plot_flag = 0
    log_area.insert(tk.END, '[INFO]: graph cleared\n')
    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : graph cleared\n" % timestamp())


# ------------------------------------------------------------------
# def open_csv()
# ------------------------------------------------------------------
# function to open & read csv file into gui
# ------------------------------------------------------------------
def open_csv():
    output_file.delete(1.0, tk.END)
    with open("csv/output.csv", 'r+', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in filereader:
            output_file.insert(tk.END, row)


# ------------------------------------------------------------------
# def timestamp()
# ------------------------------------------------------------------
# function to return current time
# ------------------------------------------------------------------
def timestamp():
    return time.strftime('%x %X')


# ------------------------------------------------------------------
# def quit_app()
# ------------------------------------------------------------------
# function to close window
# ------------------------------------------------------------------
def quit_app():
    print('quit')
    root.destroy()


# ------------------------------------------------------------------
# def plot_graphs()
# ------------------------------------------------------------------
# function to plot selected graph
# ------------------------------------------------------------------
def plot_graphs():
    # print('plotting graphs')
    global graph_select
    if graph_select.current() != 0:
        log_area.insert(tk.END, '[INFO]: graph plotted\n')
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : graph plotted\n" % timestamp())
    log_area.see(tk.END)


# ------------------------------------------------------------------
# def save_graph()
# ------------------------------------------------------------------
# function to save plotted graph
# ------------------------------------------------------------------
def save_graph():
    print('saving')
    global save_text, fig1, plot_flag
    if plot_flag != 0:  # check a graph has been generated
        if save_text.compare("end-1c", "!=", "1.0"):  # check text area is not empty
            input = save_text.get("1.0", 'end-1c')
            fig1.savefig('img/%s' % input)  # save graph using user read text
            print(input)
            log_area.insert(tk.END, '[INFO]: graph saved to \"img/%s\"\n' % input)
            save_text.delete(1.0, tk.END)
            plot_flag = 0
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : graph saved as %s\n" % (timestamp(), input))
            log_area.see(tk.END)
        else:
            log_area.insert(tk.END, '[WARN]: please enter a filename\n')
            log_area.see(tk.END)
    else:
        log_area.insert(tk.END, '[WARN]: plot a graph before saving\n')
        log_area.see(tk.END)


# ------------------------------------------------------------------
# def convert_experiment()
# ------------------------------------------------------------------
# called to convert the input experiment .txt file to .csv file
# ------------------------------------------------------------------
def convert_experiment():
    global experiment_menu
    input_file.delete(1.0, tk.END)
    output_file.delete(1.0, tk.END)
    if experiment_menu.current() == 1:  # check selected experiment
        if os.path.isfile('experiments/experiment_1.txt'):  # check file exists
            with open("experiments/experiment_1.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.convert("experiments/experiment_1.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_1.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_1.txt\" converted to csv\n"
                               % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_1.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_1.txt\" could not be found\n"
                               % timestamp())

    elif experiment_menu.current() == 2:  # check selected experiment
        if os.path.isfile('experiments/experiment_2.txt'):  # check file exists
            with open("experiments/experiment_2.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.convert("experiments/experiment_2.txt")
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_2.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_2.txt\" converted to csv\n"
                               % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_2.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_2.txt\" could not be found\n"
                               % timestamp())

    elif experiment_menu.current() == 3:  # check selected experiment
        if os.path.isfile('experiments/experiment_3.txt'):  # check file exists
            with open("experiments/experiment_3.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.convert("experiments/experiment_3.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_3.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_3.txt\" converted to csv\n"
                               % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_3.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_3.txt\" could not be found\n"
                               % timestamp())

    elif experiment_menu.current() == 4:  # check selected experiment
        if os.path.isfile('experiments/experiment_4.txt'):  # check file exists
            with open("experiments/experiment_4.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.convert("experiments/experiment_4.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_4.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_4.txt\" converted to csv\n"
                               % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_4.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_4.txt\" could not be found\n"
                               % timestamp())

    elif experiment_menu.current() == 5:  # check selected experiment
        if os.path.isfile('experiments/experiment_5.txt'):  # check file exists
            with open("experiments/experiment_5.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.convert("experiments/experiment_5.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_5.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_5.txt\" converted to csv\n"
                               % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_5.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_5.txt\" could not be found\n"
                               % timestamp())
    else:
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[ERROR] %s : (CONVERSION_ERROR) file not found - conversion aborted\n"
                           % timestamp())
        log_area.insert(tk.END, '[ERROR]: file not found - conversion aborted\n')
        print('no conversion run')
    log_area.see(tk.END)


# ------------------------------------------------------------------
# def open_log()
# ------------------------------------------------------------------
# called to display the log file in the log window
# ------------------------------------------------------------------
def open_log():
    with open("log/log_file.txt", 'r') as file:
        log_area.insert(tk.END, '\n\n===Log File Start===\n\n')
        for line in file:
            log_area.insert(tk.END, line)
        log_area.insert(tk.END, '\n===Log File End===\n\n')
    log_area.see(tk.END)


# ------------------------------------------------------------------
# def window_geometry()
# ------------------------------------------------------------------
# determines window size & position on screen
# ------------------------------------------------------------------
def window_geometry():
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    min_width = 1140
    min_height = 570
    x = w / 2 - min_width / 2
    y = h / 2 - min_height / 2
    root.geometry('%dx%d+%d+%d' % (min_width, min_height, x, y))
    root.minsize(width=min_width, height=min_height)
    # root.maxsize(width=600, height=600)


# ------------------------------------------------------------------
# def confirm_quit()
# ------------------------------------------------------------------
# generate messagebox to confirm quit
# ------------------------------------------------------------------
def confirm_quit():
    print('confirm quit')
    confirm_quit_box = tk.messagebox.askyesno(
        title='Quit?',
        message='Are you sure you want to quit?'
    )
    if confirm_quit_box is True:
        save_log()
    else:
        log_area.insert(tk.END, '[INFO]: program quit aborted\n')
        log_area.see(tk.END)


# ------------------------------------------------------------------
# def save_log()
# ------------------------------------------------------------------
# function to ask user to save the current log file
# ------------------------------------------------------------------
def save_log():
    print('save log start')
    # save the log file
    if os.path.isfile('log/log_file.txt'):
        save_log_box = tk.messagebox.askyesno(
            title='Save Log File?',
            message='Would you like to save the current log file?'
        )
        if save_log_box is True:
            timedate = time.strftime("%Y%m%d-%H%M%S")
            os.rename(r'log/log_file.txt', r'log/log_file_' + timedate + '.txt')
        else:
            print('Log file not saved')
            os.remove('log/log_file.txt')
    else:
        print('No log file found, skipping...')
    save_box()


# ------------------------------------------------------------------
# def save_box()
# ------------------------------------------------------------------
# function to ask the user to save the converted experiment file
# ------------------------------------------------------------------
def save_box():
    print('save csv start')
    # messagebox
    if os.path.isfile('csv/output.csv'):
        savebox = tk.messagebox.askyesno(
            title='Save Experiment File?',
            message='Would you like to save the converted experiment file?'
        )
        if savebox is True:
            timedate = time.strftime("%Y%m%d-%H%M%S")
            os.rename(r'csv/output.csv', r'csv/output_' + timedate + '.csv')
        else:
            if os.path.isfile('csv/output.csv'):
                os.remove('csv/output.csv')
                print('converted experiment file not saved')
                # log_area.insert(tk.END, '[INFO]: Output csv file deleted.\n')
                # no visible logging as the window is closing
        quit_app()  # call quit function

    else:
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : No converted experiment file found, skipping...\n" % timestamp())
        print('No converted experiment file found, skipping...')
        quit_app()  # call quit function


# ------------------------------------------------------------------
# def widgets()
# ------------------------------------------------------------------
# called to create all widgets in the GUI
# ------------------------------------------------------------------
def widgets():
    # menu
    menubar = tk.Menu()
    dropdown = tk.Menu(menubar, tearoff=0)
    dropdown.add_command(label="View Log", command=open_log)  # button to view log file
    dropdown.add_command(label="Reset Window", command=reset_app)  # button to reset window
    menubar.add_cascade(label="File", menu=dropdown)  # File menu
    menubar.add_cascade(label="Exit", command=confirm_quit)  # Exit button
    root.protocol("WM_DELETE_WINDOW", confirm_quit)  # calls quit function if window closed with system button
    root.config(menu=menubar)

    # left_frame_main
    # contains left_frame & left_frame1
    left_frame_main = tk.Frame(root, bg='grey', highlightthickness=0)
    left_frame_main.grid(column=0, row=0, padx=0, pady=0, sticky='nsew')

    # left_frame top
    # contains experiment selection & file viewing areas
    left_frame = tk.Frame(left_frame_main, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')

    # left_frame bottom
    # contains log area
    left_frame1 = tk.Frame(left_frame_main, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame1.grid(column=0, row=1, padx=5, pady=5, sticky='nsew')

    # right_frame
    # contains graph & related functionality
    global right_frame
    right_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    right_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')

    #####################################################
    # left_frame top widgets

    # input experiment file text area
    input_label = tk.Label(left_frame, text='Input File (.txt)')
    global input_file
    input_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=60, height=7,
                                           font='Calibri, 10', bg='black', fg='white')

    # output csv file text area
    output_label = tk.Label(left_frame, text='Output File (.csv)')
    global output_file
    output_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=60, height=7,
                                            font='Calibri, 10', bg='black', fg='white')

    # dropdown to select experiment
    experiment_label = tk.Label(left_frame, text='Choose Experiment')
    n = tk.StringVar()
    value1 = n.get()
    global experiment_menu
    experiment_menu = ttk.Combobox(left_frame, textvariable=value1)
    experiment_menu['values'] = ('Select Experiment:',
                                 'Experiment 1',
                                 'Experiment 2',
                                 'Experiment 3',
                                 'Experiment 4',
                                 'Experiment 5')
    experiment_button = tk.Button(left_frame, text="Convert", command=convert_experiment)
    experiment_menu.current(0)

    # separator
    ttk.Separator(left_frame, orient='horizontal').grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky='ew')

    # left_frame top grid placements
    input_file.grid(column=1, row=2, padx=10, pady=10, columnspan=2)
    input_label.grid(column=0, row=2, sticky='ew')
    output_file.grid(column=1, row=3, padx=10, pady=10, columnspan=2)
    output_label.grid(column=0, row=3, sticky='ew')
    experiment_label.grid(column=0, row=0, padx=10, pady=10, sticky='ew')
    experiment_menu.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
    experiment_button.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

    #####################################################
    # left_frame bottom widgets

    # log text area
    global log_area
    log_area = scrolledtext.ScrolledText(left_frame1, wrap=tk.WORD, width=60, height=10,
                                         font=('Calibri', 12), bg='black', fg='white')
    log_label = tk.Label(left_frame1, text='Log output')

    # left_frame bottom grid placements
    log_label.grid(column=0, row=0, padx=10, pady=1, sticky='ew')
    log_area.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

    #####################################################
    # right_frame widgets
    # grid placements are not separated

    # graph label
    graph_label = tk.Label(right_frame, text='Select Graph')
    graph_label.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    # dropdown to select graph type
    n = tk.StringVar()
    value2 = n.get()
    global graph_select
    graph_select = ttk.Combobox(right_frame, textvariable=value2)
    graph_select['values'] = ('Select Graph Type:',
                              'Accelerometer X',
                              'Accelerometer Y',
                              'Accelerometer Z',
                              'Temperature',
                              'Gyroscope X',
                              'Gyroscope Y',
                              'Gyroscope Z',
                              'Angle/Pitch',
                              'Roll')
    graph_select.current(0)  # set dropdown to position 0
    graph_select.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

    # button to generate graph
    graph_button = tk.Button(right_frame, text='Plot Graph', command=create_graph)
    graph_button.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

    # button to clear graph area
    clear_button = tk.Button(right_frame, text='Clear Graph', command=clear_graph)
    clear_button.grid(column=3, row=0, padx=10, pady=10, sticky='ew')

    # save graph label
    save_label = tk.Label(right_frame, text='Enter Filename to save as:')
    save_label.grid(column=0, row=3, padx=10, pady=10, sticky='ew')

    # text area used to save graph as img
    global save_text
    save_text = tk.Text(right_frame, width=20, height=1, font='Calibri, 10')
    save_text.grid(column=1, row=3, padx=10, pady=10, sticky='ew')

    # button to save the current graph
    save_button = tk.Button(right_frame, text='Save Graph', command=save_graph)
    save_button.grid(column=2, row=3, padx=10, pady=10, sticky='ew')

    # separator
    ttk.Separator(right_frame, orient='horizontal').grid(column=0, row=1, columnspan=5, padx=5, pady=5, sticky='ew')

    # create blank graph area
    global row_array, ax1, fig1
    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = fig1.add_subplot(111)
    canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(column=0, row=2, columnspan=5)

    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : widgets created\n" % timestamp())


# ------------------------------------------------------------------
# def splash_window()
# ------------------------------------------------------------------
# function to create splash screen
# ------------------------------------------------------------------
def splash_window():
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    width = 600
    height = 400
    x = w / 2 - width / 2
    y = h / 2 - height / 2

    splash.geometry('%dx%d+%d+%d' % (width, height, x, y))  # set window start position
    splash.overrideredirect(1)
    splash.configure(bg='#cf1111', highlightbackground="#cf1111", highlightthickness=2)
    splash.columnconfigure(0, weight=1)
    splash.columnconfigure(1, weight=1)
    splash.columnconfigure(2, weight=1)

    # add "Logo.png"
    image = Image.open('resource/Logo.png')
    image1 = image.resize((180, 180), resample=0)
    logo = ImageTk.PhotoImage(image1)
    label1 = tk.Label(splash, image=logo, bg='#cf1111', anchor='center')
    label1.image = logo
    label1.grid(column=1, row=0, sticky='nsew')

    # add "bar-chart.png"
    image = Image.open('resource/bar-chart.png')  # Image "bar-chart.png" made by srip from www.flaticon.com
    image1 = image.resize((220, 220), resample=0)
    logo = ImageTk.PhotoImage(image1)
    label2 = tk.Label(splash, image=logo, bg='#cf1111', anchor='center')
    label2.image = logo
    label2.grid(column=1, row=1, sticky='nsew')


# ------------------------------------------------------------------
# def main()
# ------------------------------------------------------------------
# main function
# ------------------------------------------------------------------
def main():
    root.title('Experiment Dashboard')  # set window title
    root.resizable(width=False, height=False)  # disable resizing
    root.config(bg='grey')  # set background to grey
    window_geometry()  # setup window start position
    widgets()  # create window widgets
    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window created.\n" % timestamp())


# ------------------------------------------------------------------
# Module is only run as a script or with python -m,  but not
# when it is imported.
# ------------------------------------------------------------------
if __name__ == '__main__':
    print('start\n')
    root = tk.Tk()  # create tk root
    splash = tk.Toplevel()
    splash.attributes('-topmost', True)  # set splash screen to show ontop of main window
    splash_window()  # create splash screen
    splash.after(3000, splash.destroy)  # show splash screen for 3 seconds
    main()  # call main
    log_area.insert(tk.END, "[INFO]: window created.\n")
    time.sleep(2.5)  # delay window creation by 2.5s
    root.mainloop()

    # on quit remove generated log and experiment files
    # will only run if the files have not been saved
    if os.path.isfile('log/log_file.txt'):
        os.remove('log/log_file.txt')
    if os.path.isfile('csv/output.csv'):
        os.remove('csv/output.csv')
    print('end\n')

# ------------------------------------------------------------------
# End of script
# ------------------------------------------------------------------
