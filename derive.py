"""
filename: derive.py
author: Patrick J. Ehrenreich
created: 10/26/16
modified: N/A
"""

def process(func):
    """
    Processes the function into a form which can be understood by
     the program (breaks each component into a list.)
    """
    spl_func = func.replace('^', '').split()
    return spl_func

def coef_derive(inpt):
    varfnd = 0
    power = ''
    coef = ''
    for i in range(len(inpt)):
        if inpt[i] == 'x':
            varfnd += 1
        elif varfnd == 0:
            coef += inpt[i]
        else:
            power += inpt[i]
    if int(power) - 1 == 0:
        dform = str(int(power) * int(coef))
    else:
        dform = str(int(power) * int(coef)) + 'x^' + str(int(power)-1)
    return dform


def derive(p_func):
    derived_string = ''
    for element in p_func:
        if element[0] == 'x':
            power = ''
            for i in range(1, len(element)):
                power += element[i]
            power = int(power)
            derived_string += str(power) + element[0] + '^' + str(power-1)
        elif element[0] == '+' or element[0] == '-' or element[0] == '*'\
                or element[0] == '/':
            derived_string += ' ' + element + ' '
        else:
            rtn = coef_derive(element)
            derived_string += rtn

    return derived_string


def main():
    """
    The main function should perform the following functions:
     Explain the functionalities of the application to the user
     Take user input until program is terminated by user
     Output derived functions
    """
    print('=' * 50)
    last_derived_form = ''
    while True:
        func = input('Input a function to be derived.')
        if func == 'QUIT':
            break
        if func == '':
            p_func = process(last_derived_form)
            derived_form = derive(p_func)
            last_derived_form = derived_form
            print('Derivative of', func, 'is', derived_form)
        else:
            p_func = process(func)
            derived_form = derive(p_func)
            last_derived_form = derived_form
            print('Derivative of', func, 'is', derived_form)
    print('Exiting the derivative calculator.')


if __name__ == '__main__':
    main()