t = int(input())
for nTest in range(t):
 n = int(input())
 #s = list(raw_input().strip())
 s = input().strip()
 ns = int(s) + int(s[1:]+'0') + int('0'+s[:-1])
 ss = str(ns)
 print(ss.count("0") + len(s)-len(ss))
##    answer = 0
##    for i in range(n):
##        if (i==0 or s[i-1]=='0') and (s[i]=='0') and (i==n-1 or s[i+1]=='0'):
##            answer +=1
##    print answer

