for _ in range(int(input())):
    s=input()
    l=[s[i:i+2] for i in range(len(s)-1)]
    print(len(set(l)))

