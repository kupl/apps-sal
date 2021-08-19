# cook your dish here
t = int(input())
for _ in range(t):
    arr = input()
    i = 0
    temp = []
    while i < len(arr):
        count = 0
        while i < len(arr) and arr[i] == '#':
            i += 1
        while i < len(arr) and arr[i] == '.':
            count += 1
            i += 1
        if count != 0 and count not in temp:
            temp.append(count)
    check, day = -1, 0
    for ele in temp:
        if ele > check:
            day += 1
            check = ele
    print(day)
