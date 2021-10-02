###Bogo sort in python
import random

def sort(arr):

    length = len(arr)

    while (sorted_ele(arr) == False):

        shuffle_ele(arr)

def sorted_ele(arr):

    length = len(arr)

    for i in range(0, length - 1):

        if (arr[i] > arr[i + 1]):

            return False

    return True

           

def shuffle_ele(arr):

    length = len(arr)

    for i in range(length):

        r = random.randint(0, length-1)

        arr[i], arr[r] = arr[r], arr[i]

ip_arr = [10, 2, 51, 3]

sort(ip_arr)

print("The sorted array is: ")

for i in range(0, len(ip_arr)):

    print(ip_arr[i])
