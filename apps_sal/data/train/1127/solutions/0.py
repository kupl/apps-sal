# cook your dish here
x= int(input())
for i in range(x):
    y = list(map(str, input().split()))
    j= 0
    while j<len(y)-1:
        print((y[j][0]).capitalize()+".", end=' ')
        j+= 1
    print(y[len(y)-1].capitalize())
