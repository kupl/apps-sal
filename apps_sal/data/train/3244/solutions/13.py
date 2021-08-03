def cheapest_quote(n):
    forty = int(n / 40)
    twenty = int((n - (forty * 40)) / 20)
    ten = int((n - (forty * 40) - (twenty * 20)) / 10)
    five = int((n - (forty * 40) - (twenty * 20) - (ten * 10)) / 5)
    one = int((n - (forty * 40) - (twenty * 20) - (ten * 10) - (five * 5)) / 1)
    return round((forty * 3.85) + (twenty * 1.93) + (ten * .97) + (five * .49) + (one * .1), 2)
