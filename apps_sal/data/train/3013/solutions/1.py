def delete_digit(n):
    # we just need to remove the last digit of a decreasing sequense of digits
    liststrn = list(str(n))
    for i in range(len(liststrn)):
        try:
            if liststrn[i+1] > liststrn[i]:
                return int(''.join(liststrn[:i] + liststrn[i+1:]))
        except IndexError:
            return int(''.join(liststrn[:-1]))
