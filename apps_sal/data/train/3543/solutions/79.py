import re


def increment_string(string):
    string = string[::-1]
    first_letter = re.search("\D", string)
    if first_letter is not None:
        first_letter = first_letter.span()
        substring = f"{string[first_letter[0]:]}"[::-1]
        number = f"{string[:first_letter[0]]}"[::-1]
    else:
        substring = ""
        number = string[::-1]

    # if string and the last number are detected correctly
    number_len = len(number)
    if number_len == 0:
        number = "1"
    else:
        new_number = str(int(number) + 1)
        if number_len <= len(new_number):
            number = new_number
        else:
            number = str(number[:(number_len - len(new_number))]) + new_number
    return f'{substring}{number}'
