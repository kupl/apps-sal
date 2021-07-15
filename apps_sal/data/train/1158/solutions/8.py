n = int(input())
ret = 0
while n:
 n -= 1
 num = input().split()[-1]
 if num.count('3') > num.count('5') or num.count('5') > num.count('8'):
  continue
 if num.count('3')+num.count('8')+num.count('5') != len(num):
  continue
 ret += 1
print(ret) 

