# # cook your dish here
# n,k=map(int,input().split())
# x=[int(y) for y in str(n)]
# if k<=len(x):
#     for i in range(k):
#         x[i]=9
# else:
#     k=len(x)
#     for i in range(k):
#         x[i]=9
# c="".join(str(x)for x in x)
# print(c)
# print(max(int(c),n*k))
n, k = list(map(int, input().split()))
# x=[int(y) for y in str(n)]
x = str(n)
a = []
# if k<=len(x):
#     for i in range(k):
#         x[i]=9
# else:
#     k=len(x)
#     for i in range(k):
#         x[i]=9
# print("".join(str(x)for x in x))
for i in range(len(x)):
    if k < 1:
        break
    if x[i] != '9':
        x = x[0:i] + '9' + x[i + 1:]

        k -= 1
print(x)
