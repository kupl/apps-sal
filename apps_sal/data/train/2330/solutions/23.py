s = input().strip()
n = len(s)
s = "0" + s
flag = 0
if s[n] == "1" or s[1] == "0":
    flag = 1
else:
    for i in range(1, n):
        if s[i] != s[n - i]:
            flag = 1
            break
if flag == 1:
    print((-1))
else:
    A = [1]
    for i in range(2, n):
        if s[i] == "1":
            while A:
                print((A.pop(), i))
            A = [i]
        else:
            A.append(i)
    print((n - 1, n))
