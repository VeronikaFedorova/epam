"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-',
'*','/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation
shouldn't require entering any
parameters (like -f or --function).
"""
import argparse

parser = argparse.ArgumentParser(description='Simple arithmetic operation.')
parser.add_argument('operand1', type=float, help='First operand')
parser.add_argument('operator', type=str, help='Operator')
parser.add_argument('operand2', type=float, help='Second operand')


def calculate(args):
    operand1 = args.operand1
    operand2 = args.operand2
    operator = args.operator

    math_opertions = {
        '+': lambda op1, op2: op1+op2,
        '-': lambda op1, op2: op1-op2,
        '*': lambda op1, op2: op1*op2,
        '/': lambda op1, op2: op1/op2,
    }
    operation = math_opertions.get(operator)
    if operation:
        return operation(operand1, operand2)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()