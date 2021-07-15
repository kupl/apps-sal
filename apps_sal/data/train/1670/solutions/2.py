a = input()
q=[" ", "!", "$", "%", "(", ")", "*"]
r=["%20", "%21", "%24", "%25", "%28", "%29", "%2a"]
while a[0]!="#":
    b=""
    for i in a:
        if i in q:
            b=b+r[q.index(i)]
        else:
            b=b+i
    print(b)
    a=input()

