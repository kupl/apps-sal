# cook your dish here
test_case = int(input())

for i in range(test_case):
    n = int(input())
    
    val = list(map(int, input().split(' ')))
    
    fac = 1
    for j in range(n):
        fac = fac * (j+1)
        
    noOfDigit = fac//n
    
    initialSum = 0
    
    for j in range(len(val)):
        initialSum += val[j]
        
    initialSum = initialSum*noOfDigit
    
    totalSum = 0
        
    for j in range(n):
        totalSum = totalSum + pow(10, j)*initialSum
        
    print(totalSum)
