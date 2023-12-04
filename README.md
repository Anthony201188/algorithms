# Exercise:

## Write the simple search algo to find an item in a sorted list.

Now do the same with the binary search algo.

simple_search([1,2,....,99,100], 3) ->true, number of steps

simple_search([1,2,....,99,100], 101) ->false, number of steps

binary_search([1,2,....,99,100], 3) ->true, number of steps

binary_search([1,2,....,99,100], 101) ->false, number of steps

Compare the number of steps of both algos.

run the binary_search algo for each sorted lists with the following sizes: [100, 1_000, 10_000, 100_000, 1_000_000_, 10_000_000]

### each list should start with 1

### search each list with the last element

### save the result in a results list for each list sizes 


#

## plot each your results:

### the x-axis will represent your list size
### the y-axis will represent your number of steps  
<br>

# Results:



data: [(100, 7), (1000, 10), (10000, 14), (100000, 17), (1000000, 20)

## Binary search will take only 20 steps for 1 million.

## In general, for any list of n, binary search will take 
 steps to run in the worst case, whereas simple search will take n steps.

