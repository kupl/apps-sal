n=int(input())
a=sorted(map(int,input().split()))
print((min([(a[n-1]-a[0])*(a[-1]-a[n])]+[(a[-1]-a[0])*(a[i+n-1]-a[i])
for i in range(n)])))



# Made By Mostafa_Khaled

