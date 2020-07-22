# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        # needs another loop
        mindex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mindex]:
                mindex = j
        arr[mindex], arr[i] = arr[i], arr[mindex]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # FIRST PASS - inefficient!
    # bubble sort DOES NOT need to touch last element
    # more than once! each iteration can ignore one more
    # element off the end! REDO
    swap_count = 1
    while swap_count != 0:
        swap_count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count += 1
    # for i in range(len(arr)):
    #     for j in range(len(arr) - i - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?

'''


def counting_sort(arr, maximum=9):
    # Your code here
    if len(arr) < 1:
        return []
    count_arr = [0] * (maximum + 1)
    output = [None] * (len(arr))

    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count_arr[i] += 1

    for j in range(1, len(count_arr)):
        count_arr[j] = count_arr[j] + count_arr[j - 1]

    for value, count in enumerate(count_arr):
        while count > 0 and output[count - 1] == None:
            output[count - 1] = value
            count -= 1

    return output


"""
[9, 6, 3, 7, 2, 8, 9, 2, 0, 0, 7, 1, 2, ,4 ,5 , 6] <---
max = 9
newArr = [0] * (max + 1) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
[2, 1, 3, 1, 2, 4, 1, 3, 2, 2] <-----

[2, 3, 6, 7, 9, 13, 14, 17, 19, 21] <---

[0, 0, 0, 1]
"""
