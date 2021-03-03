"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data.
The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison
functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation
shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument('operation',type=str,  help='perform operation')
parser.add_argument('nums', type=float, nargs='+')


def calculate(args):
    operation = args.operation
    nums = args.nums
    boolean_expression = False if operation in dir(math) + dir(operator) else True
    if boolean_expression:
        raise NotImplementedError
    expression = getattr(math, operation)(*nums) if operation in dir(math) else getattr(operator,operation)(*nums)
    return expression


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
