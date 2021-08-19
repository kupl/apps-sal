# cook your dish here
test = int(input())
for tt in range(0, test):
    s = input()
    n = len(s)
    p = 0
    if(s[0] == "0"):
        print(0)
    else:
        i = 0
        while(i < n and s[i] == "1"):
            i = i + 1
        while(i < n and s[i] == "0"):
            p = p + 1
            i = i + 1
        print(p)
