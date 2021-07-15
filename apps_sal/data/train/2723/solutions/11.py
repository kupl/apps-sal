from statistics import mean
D = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
L = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def average_string(s):
    try: return L[int(mean(map(D.get, s.split())))]
    except: return "n/a"
