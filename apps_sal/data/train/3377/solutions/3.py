def solve(time):
    w = ["midnight", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    h,m = map(int,time.split(":"))
    a,b = w[12] if h == 12 else w[h%12], w[h+1] if h == 11 else w[(h+1)%12]
    if m == 0: return "midnight" if h == 0 else a + " o'clock"
    elif m <= 30: return w[m]  + " minute past " + a if m == 1 else "quarter past " + a if m == 15 else "half past " + a if m == 30 else w[m] + " minutes past " + a
    else: return "quarter to " + b if m == 45 else "one minute to " + b if m == 59 else w[60-m] + " minutes to " + b
