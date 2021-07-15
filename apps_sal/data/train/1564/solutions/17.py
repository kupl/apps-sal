for a in range(int(input())):
    arr = []
    s = input().strip()
    for i in range(len(s) - 1):
        if not(s[i:i + 2] in arr):
            arr.append(s[i:i + 2])
    print(len(arr))
