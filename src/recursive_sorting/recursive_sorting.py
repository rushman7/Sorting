# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements # creates an array of zero's based on elements val ex; [0] * 4 = [0,0,0,0]
    for i in range(0, len(merged_arr)):
      if len(arrA) == 0:
        merged_arr[i] = arrB[0]
        del arrB[0]
      elif len(arrB) == 0:
        merged_arr[i] = arrA[0]
        del arrA[0]
      elif arrA[0] <= arrB[0]:
        merged_arr[i] = arrA[0]
        del arrA[0]
      elif arrA[0] >= arrB[0]:
        merged_arr[i] = arrB[0]
        del arrB[0]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)
  
  return arr


merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


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
