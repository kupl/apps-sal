def triple_trouble(one, two, three):
    arr = [one, two, three]
    result = ''

    for i in range(len(arr[0])):
        for j in range(3):
            result += arr[j][i]
    print(result)
    return result
