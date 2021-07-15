t = int(input())
for nTest in range(t):
 n = int(input())
 s = input().strip()
 ns = int(s)
 ns = ns + ns//10 + 10*ns
 
 ss = str(ns)[-n:]
 print(ss.count("0") + n-len(ss))


