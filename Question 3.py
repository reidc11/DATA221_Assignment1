#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 3: Safe Function Application
# Define a function that computes x^y. Then, given a list of pairs (x, y):
# • Use a for loop with argument unpacking to call the function.
# • Skip any pair where the exponent y is negative.
# • Store the valid results in a list and print the list.


def xSquaredByY(x, y):
    return x ** y

pairs = [[5,2], [3, -1], [4,3], [2,0]]

resultList = []

for x,y in pairs:
    if y < 0:
        continue
    resultList.append(xSquaredByY(x, y))

print(resultList)
