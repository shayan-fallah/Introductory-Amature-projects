import os.path as op
import sys


def path_input_validation(showtext, mode='a', extensions=None):
    path = input(f"{showtext} : \n>> ")
    if mode == 'a':  # Check if it is a files or directory
        while True:
            if op.isfile(path):
                extensions = op.splitext(path)[1]
                break
            elif op.isdir(path):
                break
            elif path == "Exit":
                sys.exit("Good Luck")
            else:
                print("There is no such a file or directory!, Try again or 'Exit' ")
                path = input(">> ")
        return [path, extensions]
    elif mode == 'f':  # Check if it is a file(extension necessary)
        while True:
            if op.isfile(path) and op.splitext(path)[1] in extensions:
                extensions = op.splitext(path)[1]
                break
            elif path == 'Exit':
                sys.exit("Good Luck")
            else:
                print("There is no such a file!, Try again or 'Exit' ")
                path = input(">> ")
        return [path, extensions]
    elif mode == 'd':  # Check if it is a directory
        while True:
            if op.isdir(path):
                break
            elif path == 'Exit':
                sys.exit("Good Luck")
            else:
                print("There is no such a directory!, Try again or 'Exit' ")
                path = input(">> ")
        return [path, extensions]


def input_validation(showtext, *expected_values):
    value = input(f"{showtext} \n>> ")
    while True:
        if value in expected_values:
            break
        elif value == "Exit":
            sys.exit("Good Luck")
        else:
            print("Not defined! Try again or 'Exit' ")
            value = input(">> ")
    return value
