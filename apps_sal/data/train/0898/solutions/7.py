for i in range(int(input())):
    m, n = list(map(int, input().split()))
    if n < 9:
        print(0, 0)
        continue
    k = len(str(n))
    if n == int(str(9) * k):
        ans = k
    else:
        ans = k - 1
    print(m * ans, m)
    #     res = min(m,n)
    #     res1 = res
    #     k+=1
    # else:
    #     res1 =

    # n = n//10
    # j = 1
    # while n>0:
    #     if ans==0:
    #         ans = 9*(k-j)
    #     else:
    #         temp = (ans*10+9)*(k-j)
    #         ans = ans+ min(temp,m)
    #     j+=1
    #     n = n//10
    # ans = ans+res
    # print(ans)
