def reverse_number(n):

    number = n
    is_negative = False
    if n < 0:
        is_negative = True

    number = str(number)
    number = number.strip("-")

    number = number[::-1]
    number = number.strip("0")

    if number == "":
        number = "0"

    if is_negative:
        number = "-" + number

    return int(number)
