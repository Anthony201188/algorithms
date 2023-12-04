def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result += left[i:]
    result += right[j:]

    return result
    
def merge_sort(lst):
    # exit condition: if the length of the list is 1 or less, return the list
    if len(lst) <= 1:
        return lst

    # divide the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    #  recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)
    print('left: ', left)
    print('right: ', right)

    return merge(left, right)

print(merge_sort([2,6,5,1,7,4,3]))