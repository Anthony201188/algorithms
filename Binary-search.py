# Task-1 simple search algo to find item in sorted list 

# creating a test list
test_1 = list(range(1,1000000)) 
#print(test_1)

#defining a function to find an item in the list

def simple_search(iterable, search_term):
    result = []
    count = 0
    found = False

    while found == False:
        for elm in iterable:
            count += 1
            if elm == search_term:
                result.append(elm)
                found = True
                break
    return found, count

#print(simple_search(test_1, 5))

# now do the same with a binary search which splits the iterable in half every time

def binary_search(iterable, search_term):
    count = 0
    found = False

    while found == False:

        l2 = iterable[:len(iterable)//2]
        if search_term in l2:
            count += 1
            found = True
        l3 = l2[:len(l2)//2]

        if search_term in l3:
            count += 1 
            found = True
        l4 = l3[:len(l3)//2]

        if search_term in l4:
            count += 1
            found = True

        else:
            return "Search term not found"
    

    return found, count

# note this verion doesnt work as it only tells you if the search term is within 3 smaller sections of lists, this will always be true 
#thereofer it will always take 3 steps and it will always find the segment of the list the value is in not the actual single element itself
#  unlike the verion below

#This version is a true binary search taking the middle value 
def binary_search2(iterable, search_term):
    count = 0
    found = False

    while not found and iterable: # checks both the found and the iterable variables to ensure always something is found
        middle_index = len(iterable) // 2
        middle_value = iterable[middle_index]  # finds the actuall middle value 
        
        if search_term == middle_value: # checks the middle value for the search term
            found = True
            count += 1
        elif search_term < middle_value: # if the search term is smaller than the middle value this elif slices the iterable by the middle value
            iterable = iterable[:middle_index]
            count += 1
        else:
            iterable = iterable[middle_index + 1:] # this else block slices the middle index plus 
            count += 1    # one from the iterable as the previous code shows the seach index to not be contained within 0-middle_index
            
    
    if found:
        return found, count
    else:
        return "Search term not found"

print(binary_search(test_1, 63))
print(binary_search2(test_1, 255))

