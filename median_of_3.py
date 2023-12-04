""" 
Median-of-Three: The median-of-three pivot selection strategy aims to mitigate the potential issues with the first or last element selection.
It involves selecting the median value among the first, middle, and last elements of the array as the pivot. 
This approach helps in reducing the chances of extreme imbalanced partitions.
 


EXCERSICE :
-instead of using the second element as pivot use the median of three

"""

# original
def quicksort(lst):
    if len(lst) < 2:
        return lst  #[2]
    else:
        pivot = lst[1]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater) 


# refactored quicksort function to choose median as a pivot
def quicksort_median(lst):
    if len(lst) < 2:
        return lst  #[2]
    else:
        l = len(lst)
        s = sum(lst)
        median = s // l
        pivot = lst[median]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater) 

## test case

test_lst = list(range(21)) 

quicksort_median(test_lst)





