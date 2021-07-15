def solve(time):
    harr = ["midnight", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine", "ten", "eleven", "midnight"]
    
    marr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
        "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    
    hour, minute = list(map(int,time.split(":")))
    if minute == 0:
        if hour == 0:
            return "midnight"
        return harr[hour] + " o'clock"
    if minute == 15:
        return "quarter past " + harr[hour]
    if minute == 45:
        return "quarter to " + harr[1 + hour]
    if minute == 30:
        return "half past " + harr[hour]
    if minute == 1:
        return "one minute past " + harr[hour]
    if minute == 59:
        return "one minute to " + harr[1 + hour]
    if int(int(minute) < 30):
        return marr[minute] + " minutes past " + harr[hour]
    return marr[60 - minute] + " minutes to " + harr[1 + hour]
    

