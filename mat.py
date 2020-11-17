# messagebox
if os.path.isfile('csv/output.csv'):
    savebox = messagebox.askyesno(
        title='Save File?',
        message='Would you like to save the converted experiment file?'
    )
    if savebox is True:
        timedate = time.strftime("%Y%m%d-%H%M%S")
        os.rename(r'csv/output.csv', r'csv/output_' + timedate + '.csv')
    else:
        if os.path.isfile('csv/output.csv'):
            os.remove('csv/output.csv')
            log_area.insert(tk.END, '[INFO]: Output file deleted.\n')
            # log
        with open("log/log_file.txt", 'a+') as log_file:
            log_file.write("[INFO] %s : output file deleted.\n")
    quit_app()

else:
    print('File does not exist')



    # save the log file
    if os.path.isfile('log/log_file.txt'):
        save_log_box = messagebox.askyesno(
            title='Save Log File?',
            message='Would you like to save the current log file?'
        )
    if save_log_box is True:
        timedate = time.strftime("%Y%m%d-%H%M%S")
        os.rename(r'log/log_file.txt', r'log/log_file_' + timedate + '.txt')
    else:
        print('Log file not saved')