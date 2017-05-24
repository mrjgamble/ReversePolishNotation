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
    formula = get_input()

    # Begin parsing the forumla
    stack = 


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
