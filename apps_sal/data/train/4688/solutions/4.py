def expanded_form(num):
    first_part, second_part = str(num).split(".")
    first_length = len(first_part)

    result = [
        elem + "0" * (first_length - i - 1)
        for i, elem in enumerate(first_part)
        if elem != "0"
    ]
    result += [
        elem + "/1" + "0" * (i + 1) for i, elem in enumerate(second_part) if elem != "0"
    ]

    return " + ".join(result)
