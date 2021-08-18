def name_that_number(x):
    num1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    num2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if ((x >= 0) & (x < 20)):
        return num1[x]
    else:
        if(x % 10 == 0):
            return num2[int(x / 10) - 2] + ""
        else:
            return num2[int(x / 10) - 2] + " " + num1[x % 10]
