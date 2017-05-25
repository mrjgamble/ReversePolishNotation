###################
# Reverse_polish_notation.py
#
# Cacluator that evaluates an input in reverse polish notation form
#
# Reverse Polish Notation is a mathematical notation in which every operator
# follows all of its operands.
# Source: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#

def evaluate():
    """ Evaluates a mathematical formual in RPN """

    # Define our stack to parse the input
    stack = []

    # Get the formual from the user
    formula = get_input().split()

    print(formula)

    # Begin parsing the forumla
    for i in range(len(formula)):

        # If this is a number, add it to the stack.  Otherwise, perform a
        # calculation with items in stack
        if is_number(formula[i]):
            stack.append(convert_value(formula[i]))
            print(stack)

        else:

            # Ensure parsing is correct
            if len(stack) < 2:
                print('Error - Your reverse Polish notation does not parse' +
                'correctly. Please check your input and try again.')

                return

            # retrieve values
            value2 = stack.pop()
            value1 = stack.pop()

            if formula[i] == '+':
                # do the addition
                stack.append(value1 + value2)

            elif formula[i] == '-':
                # do the subtraction
                stack.append(value1 - value2)

            elif formula[i] in ('x', 'X', '*'):
                # do the multiplication
                stack.append(value1 * value2)

            elif formula[i] == '/':
                # do the division
                if value2 == 0:
                    print('Error - Cannot divde by 0.')
                    return

                print(value1)
                print(value2)

                stack.append(value1 / value2)

            elif formula[i] == '^':
                # do the exponential
                stack.append(value1 ** value2)

            else:
                # We cannot understand the operator
                print('Error - We do not understand the operator \'' +
                formula[i] + '\'. Please check your input and try again.')

                return

    # If we have more than 1 value left, it means the RPN is incorrect.
    # Otherwise, print out the answer.
    if len(stack) > 1:
        print('Error - Your reverse Polish notation does not parse \
        correctly. Please check your input and try again')
    else:
        print('Answer: {0}'.format(stack.pop()))

def is_number(a):
    """Returns true if input value is a float or integer.  Otherwise, returns
    false.
    """
    try:
        float(a)
        return True

    except ValueError:
        return False

def convert_value(a):
    """ Appropriately converts a value from string to an integer or float"""

    if a.count('.') == 0:
        return int(a)
    else:
        return float(a)

def get_input():
    """ Prompts user to input a mathematical forumal in RPN form"""

    while True:
        notation = input('Please enter a mathematical forumal in reverse Polish notation: ')

        # We did not receive any input, so prompt again
        if not notation:
            print('\nI did not understand that. Try again.\n')
            continue
        else:
            break

    return notation

if __name__ == '__main__':
    evaluate()
