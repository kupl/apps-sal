primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def getPrimeFactors(num):
    arr = [0]*25
    for index,i  in enumerate(primes):
        if i > num:
            break
        while num%i == 0:
            arr[index]+=1
            num //= i
    return arr

def findPower(arr, mod):
    ans = 1
    for index,i in enumerate(arr):
        if i != 0:
            ans*=pow(primes[index], i, mod)
            if ans > mod:
                ans%=mod
    return ans%mod

n = int(input())
arr = list(map(int, input().strip().split()))

cumarr = []
temp = [0]*25
cumarr.append(temp.copy())

for i in arr:
    for index,p  in enumerate(primes):
        if p > i:
            break
        while i%p == 0:
            temp[index]+=1
            i //= p
    cumarr.append(temp.copy())


for x in range(int(input())):
    l, r, m = map(int, input().strip().split())
    ans = findPower([x-y for x,y in zip(cumarr[r], cumarr[l-1])], m)
    print(ans)
