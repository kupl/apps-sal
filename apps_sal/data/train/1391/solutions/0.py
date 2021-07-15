try:
 for _ in range(int(input())):
  N, K = map(int, input().split())
  cell = []
  count = 0
  l = []
  for __ in range(N):
   inserted = list(map(int, input().split()))
   cell.append(inserted)



  




  cell.sort(key=lambda x: x[1])
  time = {}

  for number in cell:
   if number[2] not in time:
    time[number[2]] = number[1]

    count += 1
   elif number[0] >= time[number[2]]:
    time[number[2]] = number[1]
    count += 1





  print(count)


except:
 pass
