# Write a code to get the input in the given format and print the output in the given format


# Input Description: First-line indicates two integers separated by space. Second-line indicates two integers
# separated by space. Third-line indicates two integers separated by space.

# Output Description:
# Print the input in the same format.

# Sample Input :
# 2 4
# 2 4
# 2 4
# Sample Output :
# 2 4
# 2 4
# 2 4

# in_value1 = tuple(map(int, input().split()))
# in_value2 = list(map(int, input().split()))
# in_value3 = set(map(int, input().split()))

# print(*in_value1)
# print(*in_value2)
# print(*in_value3)

# n = input()
numbers1 = list(map(lambda x: int(x), input().split()))
numbers2 = list(map(lambda x: int(x), input().split()))
numbers3 = list(map(lambda x: int(x), input().split()))

print(*numbers1)
print(*numbers2)
print(*numbers3)
