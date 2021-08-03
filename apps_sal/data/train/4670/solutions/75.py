def string_to_number(s):
    # ... your code here
    return (int(s))
    if s[0] == "-":
        for i, value in enumerate(s[1:]):
            number += int(value)**10 ^ (len(s) - i - 1)
        number = -1 * number

    else:

        for i, value in enumerate(s):
            print(i, value)
            number = number + int(value) * 10**(len(s) - i - 1)
            print(number, 10 ^ (len(s) - i - 1))
    return(number)
