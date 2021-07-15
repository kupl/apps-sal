# cook your dish here
def sort(array):
   new_array = []
   for i, num in enumerate(array):
      start = 0
      last = i
      while start != last:
         mid = (start + last) // 2
         if new_array[mid][0] > num[0]:
            end = mid
         else:
            start = mid + 1
      new_array.insert(start,num)
   return new_array

tests = int(input())
for _ in range(tests):
   n, m = [int(j) for j in input().split()]
   cats, rats = [[[0] * 3 for _ in range(n)],[[0] * 3 for _ in range(m)]]
   for i in range(n):
      cats[i] = [int(j) * 2 for j in input().split()]
   for i in range(m):
      rats[i] = [int(j) * 2 for j in input().split()]
   
   right_cats, left_cats, right_rats, left_rats = [[],[],[],[]]
   for i in range(n):
      start, end, time = cats[i]
      if end > start:
         right_cats.append([start-time,time,end-start+time,i])
      else:
         left_cats.append([start+time,time,start-end+time,i])
   for i in range(m):
      start, end, time = rats[i]
      if end > start:
         right_rats.append([start-time,time,end-start+time,i])
      else:
         left_rats.append([start+time,time,start-end+time,i])
   
   #right_cats = sort(right_cats)
   #right_rats = sort(right_rats)
   #left_cats = sort(left_cats)
   #left_rats = sort(left_rats)
   
   cat_number = [[-1,-1] for _ in range(m)]
   
   for rat in left_rats:
      point, start, end, index = rat
      for cat in left_cats:
         #if point < cat[0]:
         #   break
         if point == cat[0]:
            time_of_collision = max(cat[1],start)
            if time_of_collision <= end and time_of_collision <= cat[2]:
               if cat_number[index][0] == -1 or time_of_collision < cat_number[index][1]:
                  cat_number[index][0] = cat[3] + 1
                  cat_number[index][1] = time_of_collision
      for cat in right_cats:
         #if point < cat[0]:
         #   break
         time_of_collision = (point - cat[0]) // 2
         if time_of_collision >= start and time_of_collision <= end and time_of_collision >= cat[1] and time_of_collision <= cat[2]:
            if cat_number[index][0] == -1 or time_of_collision < cat_number[index][1]:
               cat_number[index][0] = cat[3] + 1
               cat_number[index][1] = time_of_collision
   for rat in right_rats:
      point, start, end, index = rat
      for cat in right_cats:
         #if point < cat[0]:
         #   break
         if point == cat[0]:
            time_of_collision = max(cat[1],start)
            if time_of_collision <= end and time_of_collision <= cat[2]:
               if cat_number[index][0] == -1 or time_of_collision < cat_number[index][1]:
                  cat_number[index][0] = cat[3] + 1
                  cat_number[index][1] = time_of_collision
      for cat in left_cats[::-1]:
         #if point > cat[0]:
         #   break
         time_of_collision = (cat[0] - point) // 2
         if time_of_collision >= start and time_of_collision <= end and time_of_collision >= cat[1] and time_of_collision <= cat[2]:
            if cat_number[index][0] == -1 or time_of_collision < cat_number[index][1]:
               cat_number[index][0] = cat[3] + 1
               cat_number[index][1] = time_of_collision
   
   for i in range(m):
      print(cat_number[i][0])
