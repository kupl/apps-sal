
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

# so the ending sequence is b...ba...a

# find length of ending sequence

extra=0
need=0
for ch in input().strip():
    if ch=='a':
        need=(need*2+1)%1000000007
    else:
        extra=(extra+need)%1000000007

print(extra)
