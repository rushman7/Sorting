# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                arr[j], arr[smallest_index] = arr[smallest_index], arr[j] 
        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        isDone = True
        largest_index = 0

        while isDone:
            if largest_index + 1 == len(arr):
                isDone = False
            elif arr[largest_index] > arr[largest_index + 1]:
                arr[largest_index], arr[largest_index + 1] = arr[largest_index + 1], arr[largest_index]
                largest_index += 1
            elif arr[largest_index] < arr[largest_index + 1]:
                largest_index += 1

    return arr
    
import random

# STRETCH: implement the Count Sort function below
def count_sort( arr ):
    # create a count array to store the count of each unique object
    if arr == []:
        return arr

    for num in range(0, len(arr)):
        if arr[num] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        
    count_array = [0 for num in range(0, max(arr) + 1)]

    # count each element in the given array and place the count at the appropriate index
    for num in range(0, len(arr)):
        count_array[arr[num]] += 1

    # modify the count array by adding the previous counts
    for num in range(0, len(count_array) - 1):
        count_array[num+1] = count_array[num] + count_array[num+1]

    # create an array based on the last index value
    new_array = [0 for num in range(0, len(arr))]

    # corresponding values represent the places in the count array
    for val in range(0, len(arr)):
        new_array[count_array[arr[val]]-1] = arr[val]
        count_array[arr[val]] -= 1

    # place the objects in their correct positions and decrease the count by one
    return new_array

