#Caitlin Reid|30245427   DATA 221 Assignment 1
# Question 7: Time Conversion Function
# Write a function that converts a given number of seconds since midnight into:
# • Hours
# • Minutes
# • Seconds
# • AM or PM
# The function should return a formatted string. If the input is invalid, return an appropriate message.


def secondsSinceMidnightTime(seconds):
    if not isinstance(seconds, int) or seconds <0 or seconds >= 86400: # input must be a positive integer, under 86400 seconds (under 24 hours)
        return "Invalid input! Please enter an integer under 86400 (24 hours)."

    hour = seconds//3600
    remainingSecondsMinusHours = seconds%3600
    minutes = remainingSecondsMinusHours//60
    finalRemainingSeconds = remainingSecondsMinusHours%60

    if hour == 0: #Case 1: Midnight (12:00AM)
        amOrPm = "AM"
        hour = 12
    elif hour == 12: #Case 2: Noon (12:00PM)
        amOrPm = "PM"
    elif hour > 12: #Case 3: Afternoon hours
        amOrPm = "PM"
        hour = hour - 12
    else: #Case 4: Morning hours
        amOrPm = "AM"

    return (f"{hour} {minutes} {finalRemainingSeconds} {amOrPm}")

#testing
print(secondsSinceMidnightTime(43932))

