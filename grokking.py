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

#print(count_items([1, 2, 3, 5, 10]))

#Find the maximum number in a list.

def highest_in_list(arr):
    if len(arr) > 1:
        if arr[0] > arr[1]:
            arr[1] = arr[0]
        return highest_in_list(arr[1:])
    else:
        return arr[0]

#print(highest_in_list([0, 5, 7, 11, 3]))

"""Remember binary search from chapter 1? It’s a divide-and-conquer
algorithm, too. Can you come up with the base case and recursive
case for binary search?"""

def binary(keyword, arr):
    mid = len(arr) // 2
    if arr[mid] == keyword:
        return f"{keyword} found in list"
    elif keyword < arr[mid]:
        return binary(keyword, arr[:mid:])
    elif keyword > arr[mid]:
        return binary(keyword, arr[mid::])
    else:
        return f"{keyword} not in list"

print(binary("giraffe", ["ant", "badger", "cat", "dog", "elephant", "ferret", "giraffe"]))