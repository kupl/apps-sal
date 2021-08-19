def delete_digit(n):
    liststrn = list(str(n))
    for i in range(len(liststrn)):
        try:
            if liststrn[i + 1] > liststrn[i]:
                return int(''.join(liststrn[:i] + liststrn[i + 1:]))
        except IndexError:
            return int(''.join(liststrn[:-1]))
