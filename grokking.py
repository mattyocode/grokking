#C&D using recursion to sum array

def addsum(arr):
    if len(arr) > 1:
        return arr.pop() + addsum(arr)
    else:
        return 0

print(addsum([1, 2, 3, 4]))