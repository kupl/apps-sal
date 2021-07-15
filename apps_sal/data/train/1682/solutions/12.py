# cook your dish here
n = str(input())
max = 0
i = 0
sum = int(n[i])
a=1
b=1
p=1
q=1
while i<len(n)-1:
    i += 1
    if int(n[i-1]) < int(n[i]):
        sum = sum + int(n[i])
        b += 1
    else:
        if sum>max:
            max=sum
            p=a
            q=b
        sum = int(n[i])
        a = i + 1
        b=a
print("{}:{}-{}".format(max,p,q))
