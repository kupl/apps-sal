# cook your dish here
t=int(input())
vowels=['a','e','i','o','u']
for i in range(t):
    s=input()
    sum=0
    for j1 in s:
        #print(ord(_)-96)
        if j1 in vowels:
            continue
        else:
            l=[]
            for k1 in vowels:
                #print(ord(k1)-96)
                if((ord(k1)-96)>=(ord(j1)-96)):
                    diff=(ord(k1)-96)-(ord(j1)-96)
                    #print(diff)
                else:
                    diff=(ord(j1)-96)-(ord(k1)-96)
                l.append(diff)
            #print(l)
            minimum=min(l)
            sum=sum+minimum
    print(sum)

