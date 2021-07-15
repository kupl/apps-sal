n=int(input())
ans=[]
for x in range(n):
    a=input()
    a=(' '.join(a.split()[::-1]))
    # print(a)
    punctuation=".,:;'"
    b=""
    for i in a:
         if i not in punctuation:
            b+=i
    ans.append(b)
n=(ans[::-1])
for i in n:
    print(i)
