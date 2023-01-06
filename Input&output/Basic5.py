# Write a code to get the input in the given format and print the output in the given format
#
#
# Input Description:
# Three integers are given in line by line.
#
# Output Description:
# Print the integers in a single line separate by space.
#
# Sample Input :
# 2
# 4
# 5
# Sample Output :
# 2 4 5

# Python program to concatenate lists
# Using itertools

import itertools

# Initializing lists
in_values1 = list(map(lambda x: int(x), input().split()))
in_values2 = list(map(lambda x: int(x), input().split()))
in_values3 = list(map(lambda x: int(x), input().split()))

# Concatenate lists using itertools
newlist = list(itertools.chain(in_values1, in_values2, in_values3))

# Print output
print('Concatenated List: ', *newlist)
#
# in_values1 = list(map(lambda x: int(x), input().split()))
# in_values2 = list(map(lambda x: int(x), input().split()))
# in_values3 = list(map(lambda x: int(x), input().split()))
# combine = in_values1 + in_values2 + in_values3
# print(*combine)
#
# # Python program to concatenate lists
# # Using extend function
#
# # Initializing lists
# list1 = [2, 3, 4, 2, 2]
# list2 = [4, 5, 6, 7, 34, 56]
# list3 = [4, 67, 2, 2, 4, 66]
#
# # concatenate lists using extend()
# list1.extend(list2)
# list1.extend(list3)
#
# # Print output
# print('Concatenated List: ', list1)
#
# # Python program to merge lists
# # Using * Operator
#
# # Initializing lists
# list1 = [2, 3, 4, 2, 2]
# list2 = [4, 5, 6, 7, 34, 56]
# list3 = [1, 5, 33, 2, 34, 46]
#
# # merge lists using * Operator
# newlist = [*list1, *list2, *list3]
#
# # Print output
# print('Concatenated List: ', newlist)
