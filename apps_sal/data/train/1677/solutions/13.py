# cook your dish here
'''
https://www.codechef.com/INOIPRAC/problems/INOI1501
'''

#inputFile = open('input.txt', 'r')
n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
ans = a[0]
diff = [0] * n
presumb = [0] * n
presumb[0] = b[0]
for i in range(1, n):
    presumb[i] = presumb[i - 1] + b[i]
mx = a[0] - presumb[0]
diff[0] = mx
for i in range(1, n):
    diff[i] = max(diff[i - 1], a[i] - presumb[i])
for i in range(1, n):
    ans = max(ans, a[i] + presumb[i - 1] + diff[i - 1])
halfmaxwraparound = [0] * n
halfmaxwraparound[0] = a[0]
totalarraysumb = presumb[n - 1]
for i in range(1, n):
    halfmaxwraparound[i] = max(halfmaxwraparound[i - 1], a[i] + presumb[i - 1])
for i in range(1, n):
    ans = max(ans, halfmaxwraparound[i - 1] + a[i] + totalarraysumb - presumb[i])


print(ans)
