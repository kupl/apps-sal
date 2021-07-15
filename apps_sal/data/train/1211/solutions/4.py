# cook your dish here
for u in range(int(input())):
    s=input()
    a=s
    for i in range(len(s)//2):
        a=a.replace("abc","")
    print(a)    
