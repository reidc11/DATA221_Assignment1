#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 2 : Nested Dictionary from Strings
# Define a function that receives a list of strings and returns a dictionary with the following struc-
# ture:
# • Each key is a string from the list.
# • Each value is another dictionary containing:
# – The length of the string
# – Whether the length is even or odd


def wordsEvenOddLength(wordList):
    outputDictionary={}

    for item in wordList:
        length = len(item)

        if length % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"

        outputDictionary[item] = {
            "Length": length,
            "Parity": parity
        }

    return outputDictionary


#Test
print(wordsEvenOddLength (["intro","to","data","science"]))
