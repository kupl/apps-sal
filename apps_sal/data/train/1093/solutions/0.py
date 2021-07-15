# # # # n = int(input())
# # # # arr = list(map(int , input().split()))
# # # # for _ in range(int(input())):
# # # # 	l,r,mod = map(int , input().split())
# # # # 	pro = 1
# # # # 	for i in range(l - 1,r):
# # # # 		pro *= arr[i]
# # # # 	print(pro % mod) #sample testcases passed #TLE
# # # import numpy #or use math
# # # n = int(input())
# # # arr = list(map(int , input().split()))
# # # for _ in range(int(input())):
# # # 	l,r,mod = map(int , input().split())
# # # 	print(numpy.prod(arr[l - 1:r]) % mod) #sample cases passed, WA
# # import math
# # primes,dic,t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],{},0
# # for i in primes:
# #     dic[i] = t
# #     t += 1
# # def primeFactors(n,arr): 
# #     for i in range(2,int(math.sqrt(n)) + 1,2): 
# #         while(n % i == 0): 
# #             arr[dic[i]] += 1 
# #             n /= i
# #     if(n > 2):
# #         arr[dic[n]] += 1
# #     return arr
# # n = int(input())
# # A = list(map(int , input().split()))
# # dp = [0]*len(primes)
# # for i in range(1,n + 1):
# #     r = [dp[i - 1]].copy()
# #     dp.append(primeFactors(A[i - 1],r))
# # for _ in range(int(input())):
# #     li,ri,m=list(map(int,input().split()))
# #     ans = 1
# #     for i in range(len(primes)):
# #         ans *= (pow(primes[i],dp[ri][i] - dp[li - 1][i],m)) % m
# #     print(ans % m) #NZEC
# import math
# primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# dic={}
# t=0
# for i in primes:
#     dic[i]=t
#     t+=1
# def primeFactors(n,arr): 
#     while(n % 2 == 0):
#         arr[dic[2]] += 1 
#         n /= 2
#     for i in range(3,int(math.sqrt(n))+1,2): 
#         while(n % i == 0): 
#             arr[dic[i]] += 1 
#             n /= i
#     if(n > 2): 
#         arr[dic[n]] += 1
#     return arr
# N = int(input())
# A = list(map(int , input().split()))
# dp = [[0]*len(primes)]
# for i in range(1,N + 1):
#     r = dp[i - 1].copy()
#     dp.append(primeFactors(A[i - 1],r))
# for _ in range(int(input())):
#     l,r,m = list(map(int , input().split()))
#     ans = 1
#     for i in range(len(primes)):
#         ans *= (pow(primes[i],dp[r][i] - dp[l - 1][i],m)) % m
#     print(ans % m)
import sys 
import math
input = sys.stdin.readline
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
dic={}
t=0
for i in primes:
    dic[i]=t
    t+=1
def primeFactors(n,arr): 
    while n % 2 == 0: 
        arr[dic[2]]+=1 
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            arr[dic[i]]+=1 
            n = n / i 

    if n > 2: 
        arr[dic[n]]+=1
    return arr
def main():
    N=int(input())
    A=list(map(int,input().split()))
    tp=[0]*len(primes)
    dp=[]
    dp.append(tp)
    for i in range(1,N+1):
        # print(i)
        r=dp[i-1].copy()
        t=primeFactors(A[i-1],r)
        dp.append(t)
    t=int(input())
    for _ in range(t):
        l,r,m=list(map(int,input().split()))
        if(m==1):
            print(0)
        else:
            ans=1
            for i in range(len(primes)):
                ans=ans*(pow(primes[i],dp[r][i]-dp[l-1][i],m))%m
            print(ans%m)
    
def __starting_point():
    main()
__starting_point()
