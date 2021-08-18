t = int(input())
for _ in range(t):
    s = input()
    k = len(s)
    count = 0
    for i in range(k - 1):
        if(s[i] == "C"):
            if(s[i + 1] == 'E' or s[i + 1] == 'S' or s[i + 1] == "C"):
                count += 1
        elif(s[i] == "E"):
            if(s[i + 1] == "S" or s[i + 1] == 'E'):
                count += 1
        elif(s[i] == "S"):
            if(s[i + 1] == "S"):
                count += 1
    if (count == k - 1):
        print("yes")
    else:
        print("no")
