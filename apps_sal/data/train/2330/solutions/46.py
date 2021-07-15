# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n = int(readline())
#*a, = map(int,readline().split())
s = input()
n = len(s)
ok = 1
if s[-1]=="1": ok = 0
if any(s[i] != s[n-2-i] for i in range(n-1)): ok = 0
if s[0]=="0": ok = 0

if ok==0:
    print("-1")
    return

e = [(0,1)]
top = 1
for i in range(1,n-1):
    e.append((top,i+1))
    if s[i]=="1":
        top = i+1

for a,b in e:
    print(a+1,b+1)
