import csv
import time
import os
import sys
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# global declarations
import conversion

global log_area, input_file, output_file, experiment_menu, right_frame, graph_select


######################################
# function to reset all widgets
######################################
def reset():
    root.quit()
    window_geometry()
    widgets()
    root.mainloop()
    # log
    with open("log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window created\n" % timestamp())


#################################################
# function to open & read csv file into gui
#################################################
def open_csv():
    output_file.delete(1.0, tk.END)
    with open("output.csv", newline='') as csvfile:
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
        with open("log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : graph plotted\n" % timestamp())
    log_area.see(tk.END)


############################################
# function to save plotted graph
############################################
def save_graph():
    print('saving')
    if graph_select.current() != 0:
        log_area.insert(tk.END, '[INFO]: graph saved\n')
        # log
        with open("log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : graph saved\n" % timestamp())
        log_area.see(tk.END)


###################################################################
# called to convert the input experiment .txt file to .csv file
###################################################################
def convert_experiment():
    global experiment_menu
    input_file.delete(1.0, tk.END)
    if experiment_menu.current() == 1:  # check selected experiment
        if os.path.isfile('experiment_1.txt'):  # check file exists
            with open("experiment_1.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.main("experiment_1.txt")  # call conversion script
                open_csv()
                log_area.insert(tk.END, "[INFO]: experiment file converted to csv")
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : experiment file converted to csv\n" % timestamp())
        else:
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : input file could not be found\n" % timestamp())

    elif experiment_menu.current() == 2:  # check selected experiment
        if os.path.isfile('experiment_2.txt'):  # check file exists
            with open("experiment_2.txt", 'r') as infile:
                input_file.insert(tk.END, infile.read())  # read file into text window
                conversion.main("experiment_2.txt")
                open_csv()
                log_area.insert(tk.END, "[INFO]: experiment file converted to csv")
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[INFO] %s : experiment file converted to csv\n" % timestamp())
        else:
            log_area.insert(tk.END, "[ERROR]: input file could not be found\n")
            log_area.see(tk.END)
            # log
            with open("log_file.txt", 'a+') as log_file:
                log_file.write("[ERROR] %s : input file could not be found\n" % timestamp())


########################################################
# called to display the log file in the log window
########################################################
def open_log():
    with open("log_file.txt", 'r') as file:
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


##################################################
# called to create all widgets in the GUI
##################################################
def widgets():
    # menu
    menubar = tk.Menu()
    dropdown = tk.Menu(menubar, tearoff=0)
    dropdown.add_command(label="View Log", command=open_log)
    dropdown.add_command(label="Reset Window", command=reset)
    dropdown.add_command(label="Quit", command=quit_app)
    menubar.add_cascade(label="File", menu=dropdown)
    root.config(menu=menubar)

    # left_frame top
    left_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ew')

    # left_frame bottom
    left_frame1 = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    left_frame1.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

    # right_frame
    global right_frame
    right_frame = tk.Frame(root, bg='#e6e6e6', highlightbackground="black", highlightthickness=2)
    right_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsw')

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
    graph_select.grid(column=1, row=0, padx=10, pady=10)

    graph_button = tk.Button(right_frame, text='Plot Graph', command=plot_graphs)
    graph_button.grid(column=2, row=0, padx=10, pady=10)

    save_button = tk.Button(right_frame, text='Save Graph', command=save_graph)
    save_button.grid(column=3, row=0, padx=10, pady=10)

    ttk.Separator(right_frame, orient='horizontal').grid(column=0, row=1, columnspan=4, padx=5, pady=5, sticky='ew')

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
    window_geometry()
    widgets()
    with open("log_file.txt", 'a+') as log_file:
        log_file.write("[INFO] %s : window created.\n" % timestamp())


if __name__ == '__main__':
    print('start\n')
    root = tk.Tk()
    main()
    log_area.insert(tk.END, "[INFO]: window created.\n")
    root.mainloop()
    # os.remove('output.csv')
    print('end\n')
