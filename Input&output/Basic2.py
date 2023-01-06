# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# A single line contains integers separated by space

# Output Description:
# Print the integer list of integers separated by space

# Sample Input :
# 2 3 4 5 6 7 8
# Sample Output :
# 2 3 4 5 6 7 8

# i_value = list(input())
# print(*i_value)

# OPEN AI PLAYGROUND
# explain the below Python code in line by line

# i_value = list(input())
# print(*i_value)

# 1. The first line creates a list called i_value and takes input from the user.
# 2. The second line prints out the elements of the list i_value, separated by a space.

i_values = list(map(int, input().split()))

print(*i_values)

# _invalue = input()
# print(*_invalue)

# year = input()
# car = ["Honda","Hyudai","Fiat","Audi","Jeep","Ferrari","Tata"]
# if year == "2015":
#    print(car[0])
# elif year == "2016":
#    print(car[1])
# elif year == "2017":
#    print(car[2])
# elif year == "2018":
#    print(car[2])
# elif year == "2019":
#    print(car[3])
# elif year == "2020":
#    print(car[4])
# elif year == "2021":
#    print(car[5])
# elif year == "2022":
#    print(car[6])
# else:
#    print("Data is not available.")
