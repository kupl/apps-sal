# @Author: Atul Sahay <atul>
# @Date:   2020-01-20T11:31:52+05:30
# @Email:  atulsahay01@gmail.com, atulsahay@cse.iitb.ac.in
# @Last modified by:   atul
# @Last modified time: 2020-01-20T23:18:12+05:30
# from operator import sub
#
# def Diff(li1, li2):
#     # print(li1)
#     # print(li2)
#     return  list(map(int.__sub__, li1,li2))
#
# def binary_search(l,val,start,end):
#     # print("start",start,"end",end)
#     # print("l",l)
#     if(start>end):
#         return 0
#     mid = (start + end) //2
#     # print("mid",mid)
#     if(l[mid] == val):
#         return (1+binary_search(l,val,start,mid-1)+binary_search(l,val,mid+1    ,end))
#     elif(l[mid]>val):
#         return (binary_search(l,val,start,mid-1))
#     else:
#         return(binary_search(l,val,mid+1,end))
#
# for t in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().strip().split()))
#     total = sum(a)
#     inter_sum = 0
#     S = 0
#     b = []
#     for i in a:
#         inter_sum+=i
#         b.append(inter_sum)
#     # print(b)
#     for i in range(n):
#         inter_sum = total - a[i]
#         if(inter_sum%2!=0):
#             continue
#         c_l = [0]*i
#         c_r = [a[i]]*(n-i)
#         c_l.extend(c_r)
#         # print(c_l)
#         l = Diff(b,c_l)
#         # print(l)
#         S+=binary_search(l,inter_sum//2,0,n-1)
#     print(S)

import bisect

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    total = sum(a)
    diff = {}
    inter_sum = 0
    for i in range(n - 1):
        if(a[i] == 0):
            continue
        inter_sum += a[i]
        c = inter_sum - (total - inter_sum)
        if(c in list(diff.keys())):
            diff[c].append(i)
        else:
            diff[c] = [i]
    count = 0
    # print(diff)
    for i in range(n):
        # print("i",i)
        if(-a[i] in list(diff.keys())):
            ans = bisect.bisect_left(diff[-a[i]], i)

            count += ans
            # print(1,ans)
        if(a[i] in list(diff.keys())):
            ans = bisect.bisect_left(diff[a[i]], i)
            count += (len(diff[a[i]]) - ans)
            # print(2,ans)
    print(count)
