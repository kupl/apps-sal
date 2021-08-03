lst = []
ans = []
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
t = int(input())
for i in range(t):
    str = input()
    s = str.lower()
    no_punct = ""
    for char in s:
        if char not in punctuations:
            no_punct = no_punct + char
    lst.extend(no_punct.split())


for i in lst:
    if i not in ans:
        ans.append(i)
ans.sort()
print(len(ans))
for j in ans:
    print(j)
