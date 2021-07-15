h={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
res=[]
T=int(input())
for i in range (T):
    s=input()
    l=len(s)
    count=0
    for j in range (l):
        count+=h[s[j]]*(16**(l-j-1))
    res.append(count)
for num in res:
    print(num)
