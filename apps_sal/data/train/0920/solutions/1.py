for _ in range(int(input())):
 string = input()
 girls,boys = string.count('g'),string.count('b')
 arrangement = ""
 answer = 0
 if(boys > girls):
  boys, girls = girls, boys
 boys_index = []
 pos = 0
 extra_right = (girls - boys) // 2
 extra_left = girls - boys - extra_right
 arrangement += 'g'*extra_left
 pos += extra_left
 for i in range(boys):
  arrangement += 'bg'
  boys_index.append(pos)
  pos += 2
 arrangement += 'g'*extra_right
 nb = 0
 ng = 0
 for i in range(len(arrangement)):
  if(arrangement[i] == 'g'):
   answer += i*nb - i*(boys-nb)
   ng += 1
  else:
   answer += i*ng - i*(girls-ng)
   nb += 1
 
 print(answer)
