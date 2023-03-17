# The Max Number
def maximum(lst):
    max_num = None
    for num in lst:
        if max_num is None or max_num < num:
            max_num = num
    return max_num


def main():
    lst1 = [1, 40, 3, 4, 300, 80, 129, 30]
    print('The Maximum Number is : ', maximum(lst1))