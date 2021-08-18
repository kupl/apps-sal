n, a = input().split()
a = int(a)
s = str(n)
while(a > 0):
    if(s[len(s) - 1] == "0"):
        s = s[:len(s) - 1]
    else:
        s1 = str((int(s[len(s) - 1])) - 1)
        s = s[:len(s) - 1]
        s = s + s1
    a = a - 1
print(int(s))
