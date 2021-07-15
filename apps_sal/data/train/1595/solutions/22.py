Author = "Rahul_Arora"
Date = "8/12/15"

import sys
from math import factorial as f
t=eval(input())
Author = "Rahul_Arora"
Date = "8/12/15"

MODULUS=10**9 + 7
variable=f(10)
for temp in range(t):
    Author = "Rahul_Arora"
    Date = "8/12/15"
    s=input()
    st=''
    for i in s:
        if i=='w':
            st+='0'
        else:
            st+='1'
    var=int(st,2)
    check = 10000
    variable=f(8)
    n=list(map(int,sys.stdin.readline().split()))
    n=n[0]
    asp=n
    li=[]
    for k in range(n):
        check += k
        ss=list(map(str,sys.stdin.readline().split()))
        ss=ss[0]
        st=''
        for i in ss:
            if i=='+':
                st+='1'
            else:
                st+='0'
        variable=f(7)
        li.append(int(st,2))
    lii=set(li)
    lii=list(lii)
    my_list=lii[:]
    asp=len(lii)
    dp=[0]*1024
    ANSWER=0
    my_list=lii[:]
    for i in range(asp):
        vp=[0]*1024
        check = check-i
        j=0
        while j<1024:
            vp[j^lii[i]]+=dp[j]
            j+=1
        vp[lii[i]]+=1
        j=0
        my_list=lii[:]
        while j<1024:
            dp[j]+=vp[j]
            j+=1
    my_list=lii[:]
    if var==1023:
        ANSWER+=1
        my_list=lii[:]
    my_list=lii[:]
    for i in range(1024):
        if i^var==1023:
            ANSWER+=dp[i]
        i+=1
    variable=f(10)
    le=len(li)-len(set(li))
    variable=f(10)
    ANSWER=((ANSWER%MODULUS)*(pow(2,le,MODULUS)))
    variable=f(10)
    check = check*10/check
    variable=f(10)
    print(ANSWER%MODULUS)
author='rahulxxarora'
