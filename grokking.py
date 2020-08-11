#Chapter 4 - Recursion. 
#Write out the code for the earlier sum function.

def addsum(arr):
    if len(arr) > 1:
        return arr.pop() + addsum(arr)
    else:
        return 0

#print(addsum([1, 2, 3, 4]))

#Write a recursive function to count the number of items in a list.

def count_items(arr):
    if len(arr) > 0:
        arr.pop()
        return 1 + count_items(arr)
    else:
        return 0

print(count_items([1, 2, 3, 5, 10]))