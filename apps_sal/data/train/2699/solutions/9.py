X = ("zero", "one", "two", "three", "four",
     "five", "six", "seven", "eight", "nine",
     "ten", "eleven", "twelve", "thirteen", "fourteen",
     "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
Y = (None, None, "twenty", "thirty", "forty",
     "fifty", "sixty", "seventy", "eighty", "ninety")


def number2words(n):
    if n < 20:
        return X[n]
    if n < 100:
        return f"{Y[n//10]}-{X[n%10]}" if n % 10 else Y[n // 10]
    if n < 1000:
        return f"{X[n//100]} hundred{f' {number2words(n%100)}' if n%100 else ''}"
    return f"{number2words(n//1000)} thousand{f' {number2words(n%1000)}' if n%1000 else ''}"
