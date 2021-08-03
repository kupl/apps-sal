def solve(s):
    arr = []
    for i in s:
        if i.isalpha():
            arr.append('*')
        else:
            arr.append(i)

    strr = ''.join(arr)

    arr = strr.split('*')

    return max([int(i) for i in arr if i != ''])
