def triple_trouble(one, two, three):
    result = ''
    for i in range(len(one)):
        result = result + one[i] + two[i] + three[i]
        print(result)
    return result
