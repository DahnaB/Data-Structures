# runtime complexity

# Efficiency: 


#lots of students chose to store the commands in a list like this
#This works but there are better options available to us.
# This is like the wrench hammering in the nail :o 
commands = ['n', 's', 'w', 'e', 'p']

selection = input()

# In the worst case, we'd have to iterate over every element in the list 
# to find what we're looking for
# So this is a Linear operation
if selection in commands:
    # if for example the input is 'w', python performs a for loop/iterates over all of the elements to see 
    #if it matches the input of 'w' that we receive 
    # this is a valid command
    # perform the user's command

#other options could have been a dictionary or set :o 

# commands = set()

# Runtime Complexity: A way to objectively measure and compare the efficiancy of two algorithms/approaches


# Complexity Classes:

# Constant Time: The efficiency DOES NOT depend on the size of the input
# Constant runtime doesn't grow at all as the size of the input increases
# Indexing into a list, accessing value via its key in a dictionary


# Linear Time: The efficiency DOES depend on the size of the input
# Linear runtime grows 1 to 1 as the size of the input increases 
# Iterating over every element in a list


# Big O ("order of") - Worst case 
# Big Theta - Average case
# Big Omega - Best case

# An example of constant time, because we are just focusing on one at the index of 3
# commands[3] # the size of the input has no bearing on the efficiency of this operation

# An example of linear time
    for command in commands: # the size of the input has direct bearing on the efficiency 
    print(command)

    for _ in commands:

# O(n) * O(1) ~ 0(n * 1) == O(n)
# Constant < Linear 

# What's being compared is how quickly the efficiency grows as a result of the input size

for _ commands: # O(n)
    # multiplies each thing by two
    #O(n) * O(n) ~ O(n * n) == O(2 * n)
    # Big O allows us to drop constants bc it only cares about the "dominating" contributor to growth

# result of this first for loop are sotred in a variable

for _ commands: O(n)
    # do something else to each of the elemtns on the result from above?

# O(n) + O(n) ~ O(n + n) == O(n^2)
