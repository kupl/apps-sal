def solve(arr):
    output = []
    for i in arr[::-1]:
        if i not in output:
            output.append(i)
        else:
            pass
    return output[::-1]
