from math import ceil
import sys
input = sys.stdin.readline

answer = []
for kek in range(int(input())):
    n = int(input())
    s = input()
    a = 0
    m = 0
    for i in s:
        if i == '(':
            a += 1
        if i == ')':
            a -= 1
        m = min(a, m)
    answer.append(-m)
print(*answer, sep='\n')
