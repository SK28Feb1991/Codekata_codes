# Write a code to get the input in the given format and print the output in the given format
#
#
# Input Description:
# A single line contains a string.
#
# Output Description:
# Print the characters in a string separated by space.
#
# Sample Input :
# guvi
# Sample Output :
# g u v i
import re

in_val1 = input()
val = ''
for i in in_val1:
    val += i + ""
print(*val)
