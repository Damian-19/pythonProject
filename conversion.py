# ------------------------------------------------------------------
# File name       : conversion.py
# ------------------------------------------------------------------
# Group number    : 1
# Group members   : Damian Larkin (18230253) & James Cusack (18250416)
# Last updated on : 08/12/2020
# Adapted from python script by Wasim Ghazal Aswad (17193559)
# ------------------------------------------------------------------
# Module description:
#   python script to satisfy project requirements for ET4244 Autumn
#   semester. Converts .txt experiment file to .csv format
# ------------------------------------------------------------------

# global declarations
global file1, file2


# ------------------------------------------------------------------
# def open_files(experiment_file)
# ------------------------------------------------------------------
# opens given experiment file & csv output file
# ------------------------------------------------------------------
def open_files(experiment_file):
    csv_file_output = 'csv/output.csv'

    global file1, file2
    file1 = open(csv_file_output, 'w')

    file2 = open(experiment_file, 'r')


# ------------------------------------------------------------------
# def main()
# ------------------------------------------------------------------
# Main script function
# ------------------------------------------------------------------
def convert(experiment_file):
    i = 0
    empty_list = []
    open_files(experiment_file)

    global file1, file2
    lines = file2.readlines()
    for line in lines:
        if 'Sample' in line:  # check if line contains 'Sample'
            i += 1
            file1.write("\n" + str(i))

        elif 'Accelerometer' in line:  # check if line contains 'Accelerometer'
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    if text == ',' or text == '-' or text == '.':
                        empty_list.append(text)

                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        if not text == '<' and not text == '>' and not text == ']':
                            if not text == '[' and not text == ' ' and not text == '=':
                                if not text == '\n':
                                    empty_list.append(text)

                    elif text.isnumeric():  # check if the text is number
                        empty_list.append(text)

        elif 'Temperature' in line:  # check if line contains 'Temperature'
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    if text == ',' or text == '-' or text == '.':
                        empty_list.append(text)

                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        if not text == '<' and not text == '>' and not text == ']':
                            if not text == '[' and not text == ' ' and not text == '=':
                                if not text == '\n':
                                    empty_list.append(text)

                    elif text.isnumeric():  # check if the text is number
                        empty_list.append(text)

        elif 'Gyroscope' in line:  # check if line contains 'Gyroscope'
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    if text == ',' or text == '-' or text == '.':
                        empty_list.append(text)

                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        if not text == '<' and not text == '>' and not text == ']':
                            if not text == '[' and not text == ' ' and not text == '=':
                                if not text == '\n':
                                    empty_list.append(text)

                    elif text.isnumeric():  # check if the text is number
                        empty_list.append(text)

        elif 'Pitch' in line:  # check if line contains 'Pitch
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    if text == ',' or text == '-' or text == '.':
                        empty_list.append(text)

                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        if not text == '<' and not text == '>' and not text == ']':
                            if not text == '[' and not text == ' ' and not text == '=':
                                if not text == '\n':
                                    empty_list.append(text)

                    elif text.isnumeric():  # check if the text is number
                        empty_list.append(text)

        if empty_list:  # check list is not empty
            # convert the list to string
            # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            print_list_to_file = ''.join(map(str, empty_list))
            file1.write(print_list_to_file)  # write list to file
            empty_list = []  # clear list

    file1.close()
    file2.close()
    print('program end')


# ------------------------------------------------------------------
# def main()
# ------------------------------------------------------------------
# main function
# ------------------------------------------------------------------
def main():
    convert()


# ------------------------------------------------------------------
# Module is only run as a script or with python -m,  but not
# when it is imported.
# ------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------------------
# End of script
# ------------------------------------------------------------------
