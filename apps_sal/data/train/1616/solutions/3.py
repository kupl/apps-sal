def parse_int(string):

    print(string)

    setDigit = {"zero": 0,
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "ten": 10,
                "eleven": 11,
                "twelve": 12,
                "thirteen": 13,
                "fourteen": 14,
                "fifteen": 15,
                "sixteen": 16,
                "seventeen": 17,
                "eighteen": 18,
                "nineteen": 19,
                "twenty": 20,
                "thirty": 30,
                "forty": 40,
                "fifty": 50,
                "sixty": 60,
                "seventy": 70,
                "eighty": 80,
                "ninety": 90,
                }

    millionNumber, thousandNumber, hundredNumber, number = (0,) * 4

    for word in string.split():
        for newWord in word.split('-'):

            try:
                digit = setDigit[newWord]
                number += digit
            except:

                if newWord == "hundred":
                    hundredNumber = number
                    number = 0

                if newWord == "thousand":
                    thousandNumber = 100 * hundredNumber + number
                    hundredNumber = 0
                    number = 0

                if newWord == "million":
                    millionNumber = number
                    number = 0

    return(millionNumber * 1000000 + thousandNumber * 1000 + hundredNumber * 100 + number)
