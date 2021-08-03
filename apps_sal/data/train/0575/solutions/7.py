# cook your dish here
import math
t = 0
try:
    t = int(input())
except EOFError as e:
    pass
for _ in range(t):
    # myStr = input().replace('=', '')
    # if len(myStr) == 0 :
    #     print(1)
    #     continue
    # ans = 0
    # count = 1
    # for k in range(len(myStr)-1):
    #     if myStr[k] == myStr[k+1]:
    #         count +=1
    #     else:
    #         ans = max(count, ans)
    #         count = 1
    #     ans = max(count, ans)
    # print(ans+1)
    s = input().replace('=', '')
    if len(s) == 0:
        print(1)
        continue
    ans, count = 0, 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            ans = max(ans, count)
            count = 1
    ans = max(count, ans)
    print(ans + 1)
