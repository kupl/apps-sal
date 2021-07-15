# cook your dish here
t = int(input())
for i in range(t):
 # n for total energy, b for energy of second screen
 n,b = map(int,input().split(" "))
 num = n//b
 final = [i*(n-b*i) for i in range(num+1)]
 print(max(final))
