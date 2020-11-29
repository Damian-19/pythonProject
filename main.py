import csv
import time
import os
import sys
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # , NavigationToolbar2Tk)

# global declarations
import conversion

global log_area, input_file, output_file, experiment_menu, right_frame, graph_select


#######################################
# graphing function
#######################################
def create_graph():
    print('plotting')
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
    for i in range(1, len(row_array)):
        # print([row_array[i][1]] + [row_array[i][2]])
        x = np.append(x, [row_array[i][1]], axis=None)
        y = np.append(y, [row_array[i][2]], axis=None)

    # y = np.array([10, 11, 12, 13, 14])
    ax1.plot(x.astype(float), y.astype(float))
    ax1.grid()
    ax1.set_title('Plot 1')
    ax1.set_xlabel('x')
    # ticks = ax1.get_xticks() * 2 * 2
    # ax1.set_xticklabels(ticks)
    ax1.set_ylabel('y')

    canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(column=0, row=2, columnspan=5)

    print('plot complete')


######################################
# function to reset all widgets
######################################
def reset_app():
    input_file.delete(1.0, tk.END)
    output_file.delete(1.0, tk.END)
    log_area.delete(1.0, tk.END)
    log_area.insert(tk.END, '[INFO]: window reset')
    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window reset\n" % timestamp())


##################################################
# function to clear the current graph area #### NOT WORKING ####
##################################################
def clear_graph():
    print('graph cleared')
    graph_select.current(0)
    log_area.insert(tk.END, '[INFO]: graph cleared\n')
    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : graph cleared\n" % timestamp())


#################################################
# function to open & read csv file into gui
#################################################
def open_csv():
    output_file.delete(1.0, tk.END)
    with open("csv/output.csv", 'r+', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in filereader:
            output_file.insert(tk.END, row)


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


######################################
# function to plot selected graph
######################################
def plot_graphs():
    print('plotting graphs')
    global graph_select
    if graph_select.current() != 0:
        log_area.insert(tk.END, '[INFO]: graph plotted\n')
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : graph plotted\n" % timestamp())
    log_area.see(tk.END)


############################################
# function to save plotted graph #### NOT WORKING ####
############################################
def save_graph():
    print('saving')
    if graph_select.current() != 0:
        log_area.insert(tk.END, '[INFO]: graph saved\n')
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : graph saved\n" % timestamp())
        log_area.see(tk.END)


###################################################################
# called to convert the input experiment .txt file to .csv file
###################################################################
def convert_experiment():
    global experiment_menu
    input_file.delete(1.0, tk.END)
    output_file.delete(1.0, tk.END)
    if experiment_menu.current() == 1:  # check selected experiment
        if os.path.isfile('experiments/experiment_1.txt'):  # check file exists
            with open("experiments/experiment_1.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.main("experiments/experiment_1.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_1.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_1.txt\" converted to csv\n" % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_1.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_1.txt\" could not be found\n" % timestamp())

    elif experiment_menu.current() == 2:  # check selected experiment
        if os.path.isfile('experiments/experiment_2.txt'):  # check file exists
            with open("experiments/experiment_2.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.main("experiments/experiment_2.txt")
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_2.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_2.txt\" converted to csv\n" % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_2.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_2.txt\" could not be found\n" % timestamp())

    elif experiment_menu.current() == 3:  # check selected experiment
        if os.path.isfile('experiments/experiment_3.txt'):  # check file exists
            with open("experiments/experiment_3.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.main("experiments/experiment_3.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: \"experiment_3.txt\" converted to csv\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : (CONVERSION) \"experiment_3.txt\" converted to csv\n" % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: \"experiment_3.txt\" could not be found\n")
            # log
            with open("log/log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : (CONVERSION_ERROR) \"experiment_3.txt\" could not be found\n" % timestamp())
    else:
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[ERROR] %s : (CONVERSION_ERROR) file not found - conversion aborted\n" % timestamp())
        log_area.insert(tk.END, '[ERROR]: file not found - conversion aborted\n')
        print('no conversion run')
    log_area.see(tk.END)


########################################################
# called to display the log file in the log window
########################################################
def open_log():
    with open("log/log_file.txt", 'r') as file:
        log_area.insert(tk.END, '\n\n===Log File Start===\n\n')
        for line in file:
            log_area.insert(tk.END, line)
        log_area.insert(tk.END, '\n===Log File End===\n\n')
    log_area.see(tk.END)


########################################################
# determines window size & position on screen
########################################################
def window_geometry():
    # window geometry
    """screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    window_width = int(910)
    window_height = int(570)
    window_x_pos = int(screen_width / 8)
    window_y_pos = int(screen_height / 20)

    print("screen height: " + str(screen_height))
    print("screen width: " + str(screen_width))
    print("window height: " + str(window_height))
    print("window width: " + str(window_width))
    root_geometry = str(window_width) + 'x' + str(window_height) + \
        '+' + str(window_x_pos) + '+' + str(window_y_pos)
    root.geometry(root_geometry)"""
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 8) - (w / 8)
    y = (hs / 8) - (h / 8)
    root.geometry('+%d+%d' % (x, y))
    # fullscreen
    # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


##########################################################
# function to ask user to save the current log file
##########################################################
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


#######################################################################
# function to ask the user to save the converted experiment file
#######################################################################
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
                # no logging as that file has already been saved
        quit_app()

    else:
        # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : No converted experiment file found, skipping...\n" % timestamp())
        print('No converted experiment file found, skipping...')
        quit_app()


##################################################
# called to create all widgets in the GUI
##################################################
def widgets():
    # menu
    menubar = tk.Menu()
    dropdown = tk.Menu(menubar, tearoff=0)
    dropdown.add_command(label="View Log", command=open_log)
    dropdown.add_command(label="Reset Window", command=reset_app)
    # dropdown.add_command(label="Quit", command=save_log)
    menubar.add_cascade(label="File", menu=dropdown)
    menubar.add_cascade(label="Exit", command=save_log)
    root.config(menu=menubar)

    # left_frame_main
    left_frame_main = tk.Frame(root, bg='grey', highlightthickness=0)
    left_frame_main.grid(column=0, row=0, padx=0, pady=0, sticky='nsew')
    # left_frame top
    left_frame = tk.Frame(left_frame_main, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')

    # left_frame bottom
    left_frame1 = tk.Frame(left_frame_main, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame1.grid(column=0, row=1, padx=5, pady=5, sticky='nsew')

    # right_frame
    global right_frame
    right_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    right_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')

    #####################################################
    # left_frame top widgets

    # input experiment file
    input_label = tk.Label(left_frame, text='Input File Text (.txt)')
    input_label.grid(column=0, row=2, sticky='ew')
    global input_file
    input_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=50, height=7,
                                           font='Calibri, 10', bg='black', fg='white')
    input_file.grid(column=1, row=2, padx=10, pady=10, columnspan=2)

    # output csv file
    output_label = tk.Label(left_frame, text='Output File Text (.csv)')
    output_label.grid(column=0, row=3, sticky='ew')
    global output_file
    output_file = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=50, height=7,
                                            font='Calibri, 10', bg='black', fg='white')
    output_file.grid(column=1, row=3, padx=10, pady=10, columnspan=2)

    experiment_label = tk.Label(left_frame, text='Choose Experiment')
    n = tk.StringVar()
    value1 = n.get()
    global experiment_menu
    experiment_menu = ttk.Combobox(left_frame, textvariable=value1)
    experiment_menu['values'] = ('Select Experiment:',
                                 'Experiment 1',
                                 'Experiment 2',
                                 'Experiment 3')
    experiment_button = tk.Button(left_frame, text="Convert", command=convert_experiment)
    experiment_menu.current(0)

    ttk.Separator(left_frame, orient='horizontal').grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky='ew')

    # left_frame grid placements
    experiment_label.grid(column=0, row=0, padx=10, pady=10, sticky='ew')
    experiment_menu.grid(column=1, row=0, padx=10, pady=10, sticky='ew')
    experiment_button.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

    #####################################################
    # left_frame bottom widgets

    global log_area
    log_area = scrolledtext.ScrolledText(left_frame1, wrap=tk.WORD, width=50, height=10,
                                         font=('Calibri', 12), bg='black', fg='white')
    log_label = tk.Label(left_frame1, text='Log output')

    log_label.grid(column=0, row=0, padx=10, pady=1, sticky='ew')
    log_area.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

    #####################################################
    # right_frame widgets

    # graph
    """fig = plt.figure(figsize=(5, 5))
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, padx=10, pady=10, columnspan=4)

    toolbar_frame = tk.Frame(master=right_frame)
    toolbar_frame.grid(column=0, row=2, columnspan=4)
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)"""

    # placeholder = tk.Text(right_frame, width=70, height=30)
    # placeholder.grid(column=0, row=2, columnspan=5, padx=5, pady=5)
    graph_label = tk.Label(right_frame, text='Select Graph')
    graph_label.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    n = tk.StringVar()
    value2 = n.get()
    global graph_select
    graph_select = ttk.Combobox(right_frame, textvariable=value2)
    graph_select['values'] = ('Select Graph Type:',
                              'Type 1',
                              'Type 2',
                              'Type 3')
    graph_select.current(0)
    graph_select.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

    graph_button = tk.Button(right_frame, text='Plot Graph', command=create_graph)
    graph_button.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

    save_button = tk.Button(right_frame, text='Save Graph', command=save_graph)
    save_button.grid(column=3, row=0, padx=10, pady=10, sticky='ew')

    clear_button = tk.Button(right_frame, text='Clear Graph', command=clear_graph)
    clear_button.grid(column=4, row=0, padx=10, pady=10, sticky='ew')

    ttk.Separator(right_frame, orient='horizontal').grid(column=0, row=1, columnspan=5, padx=5, pady=5, sticky='ew')

    # log
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : widgets created\n" % timestamp())


def main():
    root.title('Project')
    root.resizable(width=False, height=False)
    root.config(bg='grey')
    window_geometry()
    widgets()
    with open("log/log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window created.\n" % timestamp())


if __name__ == '__main__':
    print('start\n')
    root = tk.Tk()
    main()
    log_area.insert(tk.END, "[INFO]: window created.\n")
    root.mainloop()
    if os.path.isfile('log/log_file.txt'):
        os.remove('log/log_file.txt')
    if os.path.isfile('csv/output.csv'):
        os.remove('csv/output.csv')
    print('end\n')
