def QuickSort(array):
   low = 0
   high = len(array)-1
   if high > low:
        pivot = array[low]
        mid = naive(array,pivot)
        array[low:mid]  = QuickSort(array[low:mid])
        array[mid+1:] = QuickSort(array[mid+1:])
   return array

def naive(array,pivot):
    left = []
    pivots = []
    right = []

    for idx in array:
        if idx < pivot:
            left.append(idx)
        
        elif idx == pivot:
            pivots.append(idx)
        
        else:
            right.append(idx)

    #check
    array[:] = left + pivots + right
    return len(left) + len(pivots)//2

def hoare():
    pass

def dutch():
    pass


ar = [1,7,2,8,1,4,8,4,2,9]

print(QuickSort(ar))

print(ar)

