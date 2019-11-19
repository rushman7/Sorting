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
    for i in range(0, len(arr) - 1):
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


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
