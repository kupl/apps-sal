def name_that_number(num):
    num_str = str(num)
    word_num = ['zero', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    word_units = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 20:
        return word_num[num]
    else:
        first_digit = int(num_str[0]) - 2
        second_digit = int(num_str[1])
        if second_digit == 0:
            return word_units[first_digit]
        else:
            return word_units[first_digit] + ' ' + word_num[second_digit]
