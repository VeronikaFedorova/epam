"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, dest='capacity',help='Max capacity')
parser.add_argument('-w', nargs='*', type=int, dest='weights', help='list with weights')
parser.add_argument('-n', type=int, dest='bars_num', help='the amount of bars')


def handle_errors(cap, weights, num):
    if num != len(weights):
        raise ValueError
    lst_to_check = weights + [cap, num]
    for el in lst_to_check:
        if el < 0:
            raise ValueError


def bounded_knapsack(args):
    handle_errors(args.capacity, args.weights, args.bars_num)
    amount = 0
    args.weights.sort(reverse = True)

    for el in args.weights:
        if args.capacity - el >= 0:
            amount += el
            args.capacity -= el
    return amount


def main():
    try:
        args = parser.parse_args()
    except:
        raise ValueError
    print(bounded_knapsack(args=args))


if __name__ == '__main__':
    main()
