def slogans(slogan,heard):
    li = []
    while heard:
        temp = len(slogan)
        while True:
            if slogan.endswith(heard[:temp]):
                heard = heard[temp:]
                li.append(1)
                break
            temp -= 1
    return sum(li)
