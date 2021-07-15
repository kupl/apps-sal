# cook your dish here
tests = int(input())
for _ in range(tests):
   n, k = [int(j) for j in input().split()]
   nums = [int(j) for j in input().split()]
   check = [(j - (j & k)) != 0 for j in nums]
   impossible = check[0] and check[-1]
   for i in range(n-1):
      impossible = impossible or (check[i] and check[i+1])
   if impossible:
      print(-1)
   elif sum(check) != 0:
      start = -1
      for i in range(-1,n-1):
         if check[i]:
            nums[i] = nums[i-1] | nums[i+1]
            if start == -1:
               start = i+1
      for i in range(start,start+n):
         if not check[i%n]:
            nums[i%n] = nums[(i-1)%n] | nums[(i+1)%n]
      answer = 0
      for i in range(n):
         answer = answer | nums[i]
      if answer == k:
         for i in range(n):
            if check[i]:
               print(i+1, end = " ")
         for i in range(start,start+n):
            if not check[i%n]:
               print(i%n+1, end = " ")
         print("")
      else:
         print(-1)
   else:
      for i in range(-1,n-1):
         if nums[i] == nums[i] & (nums[i-1] | nums[i+1]):
            for j in range(i,i+n):
               nums[j%n] = nums[(j-1)%n] | nums[(j+1)%n]
            answer = 0
            for j in range(n):
               answer = answer | nums[j]
            if answer == k:
               for j in range(i,i+n):
                  print((j+n)%n+1,end = " ")
               print("")
            else:
               print(-1)
            impossible = True
            break
      if not impossible:
         for i in range(n):
            ss = list(nums)
            for j in range(i,i+n):
               ss[j%n] = ss[(j+1)%n] | ss[(j-1)%n]
            answer = 0
            for j in range(n):
               answer = answer | ss[j]
            if answer == k:
               for j in range(i,i+n):
                  print((j%n)+1,end=" ")
               print("")
               impossible = True
               break
      if not impossible:
         print(-1)
      
