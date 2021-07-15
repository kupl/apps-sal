# cook your dish here
for t in range(int(input())):
    str1 = input()
    new = str1.replace('abc', '')
    while new != str1:
        str1 = new
        new = str1.replace('abc', '')
    print(str1)

