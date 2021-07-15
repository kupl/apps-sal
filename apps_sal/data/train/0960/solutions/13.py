# cook your dish here
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
for tt in range(int(input())):
    n = int(input())
    cnt = 1
    for i in range(n):
        for j in range(n):
            #if j%2==0:
            #print(decimalToBinary(cnt), end=" ")
            #else:
            s = decimalToBinary(cnt)
            print(s, end=" ")
            cnt+=1
        print()
        
