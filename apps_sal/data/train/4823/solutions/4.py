from math import ceil

L = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

def wallpaper(l, w, h):
    return L[0 if not (l and w) else ceil(2*h*(l+w)*1.15/10/0.52)]
