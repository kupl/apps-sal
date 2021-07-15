bell_nums = [1]
t = [[1]]

def generate_num():
 nonlocal bell_nums
 nonlocal t
 for i in range(1,1001):
  t.append([])
  t[i].append(t[i-1][i-1])
  for j in range(1,i+1):
   t[i].append((t[i][j-1] + t[i-1][j-1]) % 1000000007)
  bell_nums.append(t[i][i])

generate_num()
tc = int(input())
while tc:
 n = int(input())
 print(bell_nums[n-1])
 tc -= 1

