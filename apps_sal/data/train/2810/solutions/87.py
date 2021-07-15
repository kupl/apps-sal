def solve(arr):
    output = []
    for string in arr:
        count = 0
        for i in range(0,len(string)):
            if ord(string[i].lower()) == (97+i):
                count += 1
        output.append(count)
    return output
