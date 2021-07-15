from math import ceil

numbers = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 
9: "nine", 10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
16:"sixteen", 17:"seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}

def wallpaper(l, w, h):
    return "zero" if w*l==0 else numbers[ceil((2*l+2*w) * h * 1.15 / 5.2)]
