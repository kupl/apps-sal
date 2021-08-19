def main():
    s = input()
    arr = []
    for i in range(len(s)):
        if len(arr) != 0 and s[i] == 'B':
            arr.pop()
        else:
            arr.append(s[i])
    print(len(arr))


for _ in range(int(input())):
    main()
