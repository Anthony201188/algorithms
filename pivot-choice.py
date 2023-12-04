""" In the Quicksort algorithm, the choice of the pivot can affect the efficiency of the sorting process:
First or Last Element: One simple approach is to select the first or last element of the array as the pivot. 
This strategy is easy to implement but can be inefficient for already sorted or nearly sorted arrays.
Random Element: Choosing a random element from the array as the pivot helps to eliminate bias in the pivot selection.
Randomized pivot selection can provide good average-case performance, but it may still suffer from poor performance in certain scenarios. 

EXCERSICE :
-instead of using the second element as pivot use a random element as pivot
-compare the performance effect with the quicksort version above

Refactor the following code:
"""

test_lst = list(range(21)) # doesnt seem to work for a list of 10k



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


# refactored quicksort to choose random element as pivot

import random

def quicksort2(lst):
    if len(lst) < 2:
        return lst  #[2]
    else:
        pivot = lst[random.randint(0, len(lst) -1 )] # this new line now uses randint function to create a random int between 0 and the lenth of lst, -1 to change the upper bound to be within valid index range (starts at 0)
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater) 


######## time test function ###########
"""
Test function uses the time module to record the time then call the test function and record the end time
execution time is the difference between the two recorded times 
input(func)-> execution time(float) 
"""

import time

def time_test(test_func, arg)-> float:
    
    start_time = time.time()  # Get the current time in seconds

    test_func(arg)  # call the test function

    end_time = time.time()  # Get the current time in seconds

    execution_time = end_time - start_time  # Calculate the time difference

    print("###########")
    print("Execution time:", execution_time, "seconds")
    print(f"Test function", test_func.__name__)
    return execution_time

###############################################

#### TESTING of execution time comparision ###

#time_test(quicksort, test_lst)
#time_test(quicksort2, test_lst)

################################################

##############################################
""" function to take a sample number of values across the range of the input test list
args:
list
y = number of sample values
returns:
meidan list
"""

def create_median_list(lst, y)->list:
    n = len(lst)
    step = n // (y + 1)
    median_list = lst[step: n - step: step]
    return median_list


##############################################

###### TESTING plotting this time testing on a graph using matplotlib ####

import matplotlib.pyplot as plt
from median_of_3 import quicksort_median # note to self cannot use kebab case for importing  use snake

test_lst = list(range(1000)) #  INPUT TEST LIST LENGTH HERE re-initialising the test list for easy changes during testing

list_lengths = create_median_list(test_lst, 40) # INPUT NUMBER OF DATA POINTS HERE creates the closest whole number second argumetn "y" median values from test_lst to plot
print(list_lengths)

execution_times_quicksort = [] # new lists to contain test results
execution_times_quicksort2 = []
execution_times_median = []


for length in list_lengths:
    execution_time_quicksort = time_test(quicksort, test_lst[:length]) # runs the quicksort function with all of the test values in list_lengths
    execution_times_quicksort.append(execution_time_quicksort) # appends the results to a singular list

    execution_time_quicksort2 = time_test(quicksort2, test_lst[:length]) # repeats the process for quicksort2
    execution_times_quicksort2.append(execution_time_quicksort2)

    execution_time_median = time_test(quicksort_median, test_lst[:length]) 
    execution_times_median.append(execution_time_median)

plt.plot(list_lengths, execution_times_quicksort, 'o-', label='Quicksort') # plots list legnths as x axis with execution_time_quicksort as y axis
plt.plot(list_lengths, execution_times_quicksort2, 'o-', label='Quicksort2 (random)') # "'o-'" specifies datapoints on the line plot
plt.plot(list_lengths, execution_times_median, 'o-', label='Quicksort_median') # newly added median function from other task
plt.xlabel('List Length') # labels the axis
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. List Length')
plt.legend() # add legend
plt.grid(True) # add grid
plt.show()