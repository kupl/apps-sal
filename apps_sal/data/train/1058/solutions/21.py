# cook your dish here
#Author : Ashutosh Wagh, Codechef : ashutosh0903
for _ in range(int(input())) :
    n = int(input())
    s = str(n)
    l = len(s)
    ans = ""
    for i in range(l) :
        ans = ans + str(int(s[i])-2)
    print(ans)

