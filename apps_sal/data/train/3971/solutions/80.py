def tidyNumber(n):
    print(n)
    for i in range(len(list(str(n)))):
        try:
            if not int(str(n)[i]) <= int(str(n)[i + 1]):
                return False
        except:
            return True
