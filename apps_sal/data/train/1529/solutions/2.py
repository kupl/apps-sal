# def toString(List):
# 	return ''.join(List)

# def permute(a, l, r):
# 	if(l==r):
# 		list_ = []
# 		list_.append(toString(a))
# 		return list_'''
# 		print(toString(a))
# 	else:
# 		for i in range(l,r+1):
# 			a[l], a[i] = a[i], a[l]
# 			permute(a, l+1, r)
# 			a[l], a[i] = a[i], a[l]

# for _ in range(int(input())):
# 	n = int(input())
# 	p = list(map(str , input().split()))
# 	permute(p, 0, n-1)
'''def permutation(start, end):
    if(end == start):
        #return a
        print(*a)
    for i in range(start, end+1):
        a[i],a[start] = a[start],a[i]
        permutation(start+1, end)
        a[i],a[start] = a[start],a[i]
for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	permutation(0,len(a)-1)'''


def factorial(n):

    f = 1
    if(n == 0 or n == 1):
        return 1
    for i in range(2, n + 1):
        f = f * i
    return f


def getSum(arr, n):

    fact = factorial(n)
    digitsum = 0
    for i in range(n):
        digitsum += arr[i]
    digitsum *= (fact // n)
    res = 0
    i = 1
    k = 1
    while(i <= n):
        res += (k * digitsum)
        k = k * 10
        i += 1

    return res


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(getSum(arr, n))
