for __ in range(int(input())):

 N, d = tuple(map(int, input().split()))

 current_num = list(map(int, list(str(N))))

 length = len(current_num)

 while True:
  for i in range(1, length + 1):

   if i == length:
    num = current_num[i - 1]
    if num > d:
     del current_num[i - 1]
     current_num.append(d)
     break
   else:
    num = current_num[i - 1]
    if num > current_num[i]:
     del current_num[i - 1]
     current_num.append(d)
     break
  else:
   break

 num = ''
 for digit in current_num:
  num += str(digit)

 print(num)
