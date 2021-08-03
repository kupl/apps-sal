def round_to_next5(n):
    result = ((n // 5) * 5)
    if ((n - ((n // 5) * 5))) > 5:
        return result - 5

    if ((n - ((n // 5) * 5))) >= 1:
        return result + 5

    if ((n - ((n // 5) * 5))) < 1:
        return result
