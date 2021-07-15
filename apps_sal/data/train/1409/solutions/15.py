# cook your dish here
import sys
#from sys import stdin,stdout
input=sys.stdin.readline
#sys.setrecursionlimit(10**7)
#import math
#import random
#import heapq
#from collections import Counter
#from queue import PriorityQueue
#from functools import lru_cache,cmp_to_key
#@lru_cache(maxsize=None) #for optimizing the execution time of callable objects/functions(placed above callable functions)

try:
    for _ in range(int(input())):
        n=int(input())
        ans=0
        while n:
            if n&1:
                ans+=1
            n=n//2
        print(ans)
        


        
except EOFError as e:
    print(e)

