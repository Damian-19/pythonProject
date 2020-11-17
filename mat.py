# ------------------------------------------------------------------
# File name       : matplotlib_1.py
# ------------------------------------------------------------------
# Group number    : ...
# Group members   : ...
# Last updated on : ...
# ------------------------------------------------------------------
# Module description:
# Python with NumPy and Matplotlib to plot the data values for the
# equation y = ax + b
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Modules to import
# ------------------------------------------------------------------

import time
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------------
# def plot_values(x, y)
# ------------------------------------------------------------------

def plot_values(x, y):
    plt.plot(x, y)
    # plt.plot(x, y, '-')
    # plt.plot(x, y, 'o')
    # plt.plot(x, y, '-o')

    plt.title('Plot of y vs. x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


# ------------------------------------------------------------------
# def main()
# ------------------------------------------------------------------
# Main script function
# ------------------------------------------------------------------

def main():
    print('Start script run %s ' % time.strftime('%c'))

    a = 4
    b = 5
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    x_data = np.array(x)

    y_data = (a * x_data) + b

    print(a)
    print(b)
    print(x)
    print(x_data)
    print(y_data)

    plot_values(x_data, y_data)

    print('End script run %s ' % time.strftime('%c'))


# ------------------------------------------------------------------
# Module is only run as a script or with python -m,  but not
# when it is imported.
# ------------------------------------------------------------------

if __name__ == '__main__':
    main()

# ------------------------------------------------------------------
# End of script
# ------------------------------------------------------------------
