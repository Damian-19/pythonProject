# ------------------------------------------------------------------
# File name       : main.py
# ------------------------------------------------------------------
# Group number    : 1
# Group members   : Damian Larkin (18230253) & James Cusack (18250416)
# Last updated on : 02/12/2020
# ------------------------------------------------------------------
# Module description:
#   python script to satisfy project requirements for ET4244 Autumn
#   semester. Converts .txt experiment file to .csv format
# ------------------------------------------------------------------

global file1, file2


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
        if 'Sample' in line:
            i += 1
            file1.write("\n" + str(i))
        elif 'Accelerometer' in line:
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    # check text = , or - or .
                    if text == ',' or text == '-' or text == '.':
                        # add text to list
                        empty_list.append(text)

                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        if not text == '<' and not text == '>' and not text == ']':
                            if not text == '[' and not text == ' ' and not text == '=':
                                # check if the text is not \n (new line)
                                if not text == '\n':
                                    # add the text to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(text)

                    # check if the text is number
                    elif text.isnumeric():
                        # add text to list
                        empty_list.append(text)

        # To check if it was there 'Temperature' word
        elif 'Temperature' in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    # check if the text = , or - or .
                    if text == ',' or text == '-' or text == '.':
                        # add the text to the empty list
                        empty_list.append(text)
                    # check if the text not number or alphabet
                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        # check if the text not < or > or ]
                        if not text == '<' and not text == '>' and not text == ']':
                            # check if the text not space or [ or =
                            if not text == '[' and not text == ' ' and not text == '=':
                                # check if the text is not \n (new line)
                                if not text == '\n':
                                    # add the text to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(text)
                    # check if the text is number
                    elif text.isnumeric():
                        # add the text to the empty list
                        empty_list.append(text)
        # To check if it was there 'Gyroscope' word
        elif 'Gyroscope' in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    # check if the text = , or - or .
                    if text == ',' or text == '-' or text == '.':
                        # add the text to the empty list
                        empty_list.append(text)
                    # check if the text not number or alphabet
                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        # check if the text not < or > or ]
                        if not text == '<' and not text == '>' and not text == ']':
                            # check if the text not space or [ or =
                            if not text == '[' and not text == ' ' and not text == '=':
                                # check if the text is not \n (new line)
                                if not text == '\n':
                                    # add the text to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(text)
                    # check if the text is number
                    elif text.isnumeric():
                        # add the text to the empty list
                        empty_list.append(text)
        # To check if it was there 'Pitch' word
        elif 'Pitch' in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    text = (x[number])
                    # check if the text = , or - or .
                    if text == ',' or text == '-' or text == '.':
                        # add the text to the empty list
                        empty_list.append(text)
                    # check if the text not number or alphabet
                    elif not text.isnumeric() and not text.isdigit() \
                            and not text.isalpha():
                        # check if the text not < or > or ]
                        if not text == '<' and not text == '>' and not text == ']':
                            # check if the text not space or [ or =
                            if not text == '[' and not text == ' ' and not text == '=':
                                # check if the text is not \n (new line)
                                if not text == '\n':
                                    # add the text to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(text)
                    # check if the text is number
                    elif text.isnumeric():
                        # add the text to the empty list
                        empty_list.append(text)
        # check if the empty_list is not empty

        if empty_list:
            # convert the list to string
            # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            print_list_to_file = ''.join(map(str, empty_list))
            # write the string print_list_to_file to the file
            file1.write(print_list_to_file)
            # delete all the element on the list
            empty_list = []

    file1.close()
    file2.close()
    print('program end')


def main():
    convert()


if __name__ == '__main__':
    main()
