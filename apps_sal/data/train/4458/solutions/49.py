import re

def time_correct(t):
    pattern = r"^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]$"

    if t == "":
        return ""
    elif t == None:
        return None

    if re.match(pattern, t):
        time = t.split(":")

        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])

        if second >= 60:
            second = second % 60
            carry = 1
            minute = minute + carry
            carry = 0

        if minute >= 60:
            minute = minute % 60
            carry = 1
            hour = hour + carry

        if hour >= 24:
            hour = hour % 24

        hour = str(hour)
        minute = str(minute)
        second = str(second)
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
        if len(second) == 1:
            second = "0" + second

        return hour + ":" + minute + ":" + second
    else:
        return None
