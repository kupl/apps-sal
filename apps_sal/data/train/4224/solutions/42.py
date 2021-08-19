def dont_give_me_five(start, end):
    countnotfive = 0
    for scanner in range(start, end + 1):
        if '5' not in str(scanner):
            countnotfive += 1
    return countnotfive


print(dont_give_me_five(52, 106))
