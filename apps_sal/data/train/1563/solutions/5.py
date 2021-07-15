for case in range(int(input())):
 a,b = input().split()
 print(str(int(a[::-1]) + int(b[::-1]))[::-1].lstrip("0"))
