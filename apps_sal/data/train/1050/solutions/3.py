# cook your dish here
t=int(input())
for _ in range(t):
    s = input()
    count = 0
    l = []
    for i in range(0,len(s)):
        #print(l)
        if s[i] == ">":
            
            if len(l)!=0 and l[-1]=="<":
                #("jk")
                l.pop()
                if len(l)==0:
                    count = i+1
            else:
                break
                    
            
        else:
            l.append("<")
    print(count)
