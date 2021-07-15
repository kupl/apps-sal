def solve(time):
    harr = ["midnight", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine", "ten", "eleven", "midnight"]
    
    marr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
        "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    
    hour = time[:2]
    minute = time[3:]
    if minute == "00":
        if hour == "00":
            return "midnight"
        return harr[int(hour)] + " o'clock"
    if minute == "15":
        return "quarter past " + harr[int(hour)]
    if minute == "45":
        return "quarter to " + harr[1 + int(hour)]
    if minute == "30":
        return "half past " + harr[int(hour)]
    if minute == "01":
        return "one minute past " + harr[int(hour)]
    if minute == "59":
        return "one minute to " + harr[1 + int(hour)]
    if int(int(minute) < 30):
        return marr[int(minute)] + " minutes past " + harr[int(hour)]
    return marr[60 - int(minute)] + " minutes to " + harr[1 + int(hour)]
    

