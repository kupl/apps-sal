def caffeineBuzz(n):
    result = "mocha_missing!"
    if not n % 3:
        if not n % 4:
            result = "Coffee"
        else:
            result = "Java"

        if not n % 2:
            result = ''.join((result, "Script"))

    return result
