lessThan20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def name_that_number(n):
    if n == 0:
        return "zero"
    return helper(n).strip()


def helper(n):
    if n < 20:
        return lessThan20[n] + " "
    return tens[n // 10] + " " + helper(n % 10)
