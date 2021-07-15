# your code goes here
test_cases = int(input())
for i in range(0,test_cases):
 num_digits = int(input())
 input_str = input()
 digits_old = input_str.split()
 digits = []
 num_zero = 0
 for num in digits_old:
  if num == '0':
   num_zero += 1 
  digits.append(int(num))
 if num_zero == 0:
  print(-1)
 else:
  digits.sort(reverse = True)
  start = True
  flag = 1
  while start or number != 0:
   start = False
   number = 0
   sum_digits = 0
   for num in digits:
    sum_digits += num
    number = number*10 + num
   if sum_digits%3 == 0:
    print(number)
    flag = 0
    break
   if digits[num_digits-1-num_zero] in [0,3,6,9]:
    num_zero += 1
    continue
   del digits[num_digits-1-num_zero]
   num_digits -= 1
  if flag == 1:
   print(0)
