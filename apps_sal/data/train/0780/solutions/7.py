c = eval(input())
for _ in range(c):
 a,b = list(map(int,input().split()))
 print({False:'ODD',True:'EVEN'}[(a%b)&0x01 == 0x00])

