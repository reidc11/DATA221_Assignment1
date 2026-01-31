#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 5: Circle Area Comparison with Validation
# Write a function that takes the radii of two circles and performs the following:
# • Validates that both radii are positive integers.
# • Computes the area of each circle.
# • Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
# If invalid input is provided, return a meaningful message instead of performing the calculation.


import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Invalid input! Radii must be positive integers!"

    if (radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0):
        return "Invalid input! Radii must be positive integers!"


    radiusOneArea = math.pi*radiusOfCircle1**2
    radiusTwoArea = math.pi*radiusOfCircle2**2

    smallerArea = min(radiusOneArea, radiusTwoArea)
    largerArea = max(radiusOneArea, radiusTwoArea)

    percentageLargerCircleCoverage = (smallerArea/largerArea)*100

    return percentageLargerCircleCoverage

print(circleAreaCoverage(5, 10))


