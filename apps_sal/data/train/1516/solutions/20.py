# t=int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     summation=0
#     last_term=k-1
#     common_difference=n-1
#     first_term=last_term%common_difference
#     if first_term==0:
#         first_term=common_difference
#     no_of_terms=(last_term-first_term)//common_difference + 1
#     #print(no_of_terms,first_term,last_term,common_difference)
#     summation=(((no_of_terms)*(first_term+last_term))//2)%1000000007
#     print(summation)
#
# import math
#
# MOD = 1000000007
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     first = k - 1;
#     diff = n - 1;
#     t = (first + diff) // (diff)
#     # print(t)
#     y = (2 * (first) - (t - 1) * (diff))
#     if (y % 2 == 0):
#         y = y // 2;
#     else:
#         t = t // 2;
#
#     ans = y * t;
#     ans = ans % MOD
#     # print("n,k:"+str(n)+" "+str(k))
#     print(ans)
MOD = 1000000007
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 2:
        last_term = k - 1
        first_term = 1
        no_terms = last_term
        ans = (last_term * (last_term + 1)) // 2
        print(ans % MOD)

    else:
        print(1)
