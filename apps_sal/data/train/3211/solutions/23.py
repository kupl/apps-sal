def divide(weight):
    x = weight / 2
    y = weight // 2
    if weight == 2:
        answer = False
    elif x == y:
        answer = True
    elif x != y:
        answer = False
    return(answer)
