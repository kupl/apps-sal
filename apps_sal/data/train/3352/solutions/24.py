def find_longest(arr):
   weishu = [1]
   for number in arr:
       count = 0
      # print(number)
      # number = int(number)
       while number != 0:
           number = number // 10
           #print(number)
           count = count + 1
       #print(count)
      # print(weishu)
       weishu.append(count)
       #print(weishu)
   a = max(weishu)
   #print(a)
  #print(arr)
   for number1 in arr:
        number = number1
        count = 0
       # number = int(number)
        while number != 0:
           number = number // 10
           count = count + 1
        print(count)
        if count  == a:
          return number1
