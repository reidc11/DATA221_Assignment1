#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 7: Time Conversion Function
# Write a function that converts a given number of seconds since midnight into:
# • Hours
# • Minutes
# • Seconds
# • AM or PM
# The function should return a formatted string. If the input is invalid, return an appropriate message.

##what is invalid input? not numbers? What if number of seconds is greater than the amount in 24 hours?

def secondsSinceMidnightTime(seconds):
    hour = seconds//3600
    remainingSecondsMinusHours = seconds%3600
    minutes = remainingSecondsMinusHours//60
    finalRemainingSeconds = remainingSecondsMinusHours%60

    if hour > 12:
        amOrPm = "PM"
        hour = hour - 12
    else:
        amOrPM = "AM"

    return (f"{hour} {minutes} {finalRemainingSeconds} {amOrPM}")

#testing
print(secondsSinceMidnighTime(82623))

