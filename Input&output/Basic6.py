# Write a code to get the input in the given format and print the output in the given format
#
#
# Input Description: First-line indicates two integers separated by space. Second-line indicates three integers
# separated by space. Third-line indicates three integers separated by space
#
# Output Description:
# Print the input in the same format.
#
# Sample Input :
# 2 5
# 2 5 6
# 2 4 5
# Sample Output :
# 2 5
# 2 5 6
# 2 4 5

in_val1 = list(map(lambda x: int(x), input().split()))
in_val2 = tuple(map(lambda x: int(x), input().split()))
in_val3 = set(map(lambda x: int(x), input().split()))

print(*in_val1)
print(*in_val2)
print(*in_val3)
