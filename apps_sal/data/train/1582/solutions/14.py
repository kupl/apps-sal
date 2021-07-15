# cook your dish here
n=int(input())
ar=input()
count=0
for x in range(1,n):
    if ar[x]==ar[x-1]:
        count+=1
print(count)
