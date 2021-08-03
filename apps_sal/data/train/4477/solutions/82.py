def reverse_number(n):

    result = ""

    if n == 0:

        return 0

    elif n > 0:  # positive number case
        result = str(n)[::-1]

        return(int(result))

    else:
        result = (str(n)[1::])[::-1]  # negative number case

        return(int(result) * -1)
