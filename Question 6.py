#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 6: Distribution Analysis
# Define a function that receives a list of numbers and returns a dictionary where:
# • Each key is a unique value from the list.
# • Each value is the percentage of elements in the list that are less than or equal to that key.
# The resulting dictionary should be sorted by key before being returned

#What is 'the list" the input list or the sorted no duplicates

 def distributionAnalysisOfList(numberList):
     sortedNoDuplicatesNumberList = []
     for number in numberList:
         if number not in sortedNoDuplicatesNumberList:
             sortedNoDuplicatesNumberList.append(number)
     sortedNoDuplicatesNumberList.sort()

     totalCount = len(sortedNoDuplicatesNumberList)

     for number in sortedNoDuplicatesNumberList:
         count = 0
         for nu
         outputDictionary(number) = {number, }



