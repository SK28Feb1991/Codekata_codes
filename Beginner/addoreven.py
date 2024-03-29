# You are provided with a number check whether its odd or even.
#
# Print "Odd" or "Even" for the corresponding cases.
#
# Note: In case of a decimal, Round off to the nearest integer and then find the output. Incase the input is zero,
# print "Zero".
#
#
# Input Description:
# A number is provided as the input.
#
# Output Description: Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases.
# Note: In case of a decimal, Round off to the nearest integer and then find the output. In case the input is zero,
# print "Zero".
#
# Sample Input :
# 2
# Sample Output :
# Even

a = int(input())
b = round(a % 2)
if a == 0:
    print("Zero")
elif b == 0:
    print("Even")
else:
    print("Odd")
