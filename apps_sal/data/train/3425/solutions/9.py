def word_square(letters):
    l = [letters.count(x) for x in set(letters)]
    if int(len(letters) ** 0.5) ** 2 == len(letters):
        if sum((x for x in l if x == 1)) <= int(len(letters) ** 0.5):
            return True
        else:
            return False
    else:
        return False
