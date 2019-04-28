import math
import os


def proccessInput(input_file):
    f = open(input_file)
    input = f.read().splitlines()
    list = []
    n = int(input[0])

    # Linear Time complexity O(n): time execution proportional to list size
    for i in range(1, n + 1):  
        action = input[i].split(' ')[0]
        value = int(input[i].split(' ')[1])

        if action == 'a':
            list.append(value)
            print(calculateMedian(list))

        if action == 'r':
            if value not in list:
                print('Wrong!')
            else:
                 # Linear Time complexity O(n): time execution proportional to list size
                list.remove(value) 
                print(calculateMedian(list))


def calculateMedian(list):
    list.sort()  # time complexity n log2 n
    l = len(list)  # time complexity O(1) constant time, fast - no cost

    # if empty list return wrong
    if l == 0:
        return 'Wrong!'

    # if odd...
    if not l % 2 == 0:
        m = list[ int(math.floor(l/2)) ]
    else:  # is even
        idx1 = int(l / 2)
        idx2 = idx1 - 1

        m = (list[idx1] + list[idx2]) / 2

        # removes decimal point on ints
        if (list[idx1] + list[idx2]) % 2 == 0:
            m = int(str(m)[0])

    return m


proccessInput(os.path.dirname(os.path.abspath(__file__)) + '/input.txt')
