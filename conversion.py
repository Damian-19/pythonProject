#######################################
# txt to csv conversion
# Author: Damian Larkin (18230253)
#######################################
import time
import csv


def main(experiment_file):
    i = 0
    empty_list = []
    # output in CSV for experiment results
    csv_file_output = "output.csv"
    # experiment_file

    file1 = open(csv_file_output, 'w')

    file2 = open(experiment_file, "r")
    lines = file2.readlines()
    for line in lines:
        if "Sample" in line:
            i += 1
            file1.write("\n" + str(i))
        elif "Accelerometer" in line:
            for row in line:
                x = ','.join(row)
                for number in range(0, len(x)):
                    number_or_char = (x[number])
                    # check if the number_or_char = , or - or .
                    if number_or_char == ',' or number_or_char == '-' or number_or_char == '.':
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
                    # check if the number_or_char not number or alphabet
                    elif not number_or_char.isnumeric() and not number_or_char.isdigit() and not number_or_char.isalpha():
                        # check if the number_or_char not < or > or ]
                        if not number_or_char == '<' and not number_or_char == '>' and not number_or_char == ']':
                            # check if the number_or_char not space or [ or =
                            if not number_or_char == '[' and not number_or_char == ' ' and not number_or_char == '=':
                                # check if the number_or_char is not \n (new line)
                                if not number_or_char == '\n':
                                    # add the number_or_char to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(number_or_char)
                    # check if the number_or_char is number
                    elif number_or_char.isnumeric():
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
        # To check if it was there 'Temperature' word
        elif "Temperature" in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    number_or_char = (x[number])
                    # check if the number_or_char = , or - or .
                    if number_or_char == ',' or number_or_char == '-' or number_or_char == '.':
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
                    # check if the number_or_char not number or alphabet
                    elif not number_or_char.isnumeric() and not number_or_char.isdigit() and not number_or_char.isalpha():
                        # check if the number_or_char not < or > or ]
                        if not number_or_char == '<' and not number_or_char == '>' and not number_or_char == ']':
                            # check if the number_or_char not space or [ or =
                            if not number_or_char == '[' and not number_or_char == ' ' and not number_or_char == '=':
                                # check if the number_or_char is not \n (new line)
                                if not number_or_char == '\n':
                                    # add the number_or_char to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(number_or_char)
                    # check if the number_or_char is number
                    elif number_or_char.isnumeric():
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
        # To check if it was there 'Gyroscope' word
        elif "Gyroscope" in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    number_or_char = (x[number])
                    # check if the number_or_char = , or - or .
                    if number_or_char == ',' or number_or_char == '-' or number_or_char == '.':
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
                    # check if the number_or_char not number or alphabet
                    elif not number_or_char.isnumeric() and not number_or_char.isdigit() and not number_or_char.isalpha():
                        # check if the number_or_char not < or > or ]
                        if not number_or_char == '<' and not number_or_char == '>' and not number_or_char == ']':
                            # check if the number_or_char not space or [ or =
                            if not number_or_char == '[' and not number_or_char == ' ' and not number_or_char == '=':
                                # check if the number_or_char is not \n (new line)
                                if not number_or_char == '\n':
                                    # add the number_or_char to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(number_or_char)
                    # check if the number_or_char is number
                    elif number_or_char.isnumeric():
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
        # To check if it was there 'Pitch' word
        elif "Pitch" in line:
            # Read first row from the file
            for row in line:
                # Store each object in the variable X
                x = ','.join(row)
                for number in range(0, len(x)):
                    number_or_char = (x[number])
                    # check if the number_or_char = , or - or .
                    if number_or_char == ',' or number_or_char == '-' or number_or_char == '.':
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
                    # check if the number_or_char not number or alphabet
                    elif not number_or_char.isnumeric() and not number_or_char.isdigit() and not number_or_char.isalpha():
                        # check if the number_or_char not < or > or ]
                        if not number_or_char == '<' and not number_or_char == '>' and not number_or_char == ']':
                            # check if the number_or_char not space or [ or =
                            if not number_or_char == '[' and not number_or_char == ' ' and not number_or_char == '=':
                                # check if the number_or_char is not \n (new line)
                                if not number_or_char == '\n':
                                    # add the number_or_char to the empty list just to be sure it will add just the
                                    # Comma and Negative sign then it will add to empty list
                                    empty_list.append(number_or_char)
                    # check if the number_or_char is number
                    elif number_or_char.isnumeric():
                        # add the number_or_char to the empty list
                        empty_list.append(number_or_char)
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
    print("######CONVERSION END#######")


if __name__ == '__main__':
    main()

# ####################################
# END
