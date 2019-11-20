# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements # creates an array of zero's based on elements val ex; [0] * 4 = [0,0,0,0]
    # TO-DO
    for i in range(0, len(merged_arr)):
      if  len(arrA) == 0:
        merged_arr[i] = arrB[0]
      elif len(arrB) == 0:
        merged_arr[i] = arrA[0]
      elif arrA[0] <= arrB[0]:
        merged_arr[i] = arrA[0]
        del arrA[0]
      elif arrA[0] >= arrB[0]:
        merged_arr[i] = arrB[0]
        del arrB[0]

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # divide in half until you have subarrays of length 1
    # merge sorted lists together
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


merge([3, 5, 6, 11], [5, 6, 7, 10])