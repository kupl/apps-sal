'''
Created on Oct 9, 2012

@author: Nitish
'''

def solve():
    levels = {}
    power = 0
    N, M = list(map(int, input().split()))
    for i in range(N):
        C, L = list(map(int, input().split()))
        if L in levels:
            levels[L] += C 
        else:
            levels[L] = C
    for f in range(M):
        C, L = list(map(int, input().split()))
        levels[L] -= C
    
    for key, value in list(levels.items()):
        if value < 0:
            power += value
    
    print(abs(power))    

def __starting_point():
    T = int(input())
    while T > 0:
        solve()
        T -= 1
__starting_point()
