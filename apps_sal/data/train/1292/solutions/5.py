# cook your dish here
def suma(s, e, cnt):
 t = e - s
 if cnt < e:
  t_1 = e - cnt + 1
  ans = t * (t + 1) // 2 - t_1 * (t_1+1) // 2
 else:
  ans = t * (t + 1) // 2 - 1
 return ans

n, m, w, b, *l = list(map(int, input().split()))
# mat = [[0 for _ in range(m)] for _ in range(n)]
dic = {}
for i in range(0, 2*w, 2):
 y, x = l[i]-1, l[i+1]-1
 # mat[y-1][x-1] = 1
 if y not in dic:
  dic[y] = [[x, 1]]
 else:
  dic[y].append([x, 1])

for i in range(2*w, 2*(w+b), 2):
 y, x = l[i]-1, l[i+1]-1
 # mat[y-1][x-1] = 2
 if y not in dic:
  dic[y] = [[x, 2]]
 else:
  dic[y].append([x, 2])

ans = 0
for v in list(dic.values()):
 v.sort()
 v.append([m-1, 2])
 i = len(v) - 1
 cnt_i = m + 1
 ans += 1
 while i >= 0:
  if i-1 >= 0 and v[i - 1][1] == 2:
   ans += suma(v[i - 1][0], v[i][0], cnt_i)
   cnt_i = v[i-1][0]
   i -= 1
  elif i-2 >= 0 and v[i - 2][1] == 1:
   ans += suma(v[i - 2][0], v[i][0], cnt_i)
   if cnt_i != v[i - 1][0]:
    ans -= (v[i][0] - v[i - 1][0] + 1)
   cnt_i = v[i - 2][0]
   i -= 1
  elif i-2 >= 0 and v[i - 2][1] == 2:
   ans += suma(v[i - 2][0], v[i][0], cnt_i)
   if cnt_i != v[i - 1][0]:
    ans -= (v[i][0] - v[i - 1][0] + 1)
   cnt_i = v[i - 2][0]
   i -= 2
  else:
   ans += suma(-1, v[i][0], cnt_i)
   if i == 1 and cnt_i != v[i - 1][0]:
    ans -= (v[i][0] - v[i - 1][0] + 1)
   break

 # prev_w = -1
 # blk = m - 1
 # cnted_i = m
 # for i in range(len(v) - 1, -1, -1):
 #     prev_blk = -1
 #     if v[i][1] == 2:
 #         prev_blk = blk
 #         blk = v[i][0]
 #         prev_w = -1
 #         ans -= 1
 #     elif v[i][1] == 1:
 #         if prev_w != -1:
 #             prev_blk = blk
 #             blk = prev_w
 #             ans -= 1
 #         prev_w = v[i][0]
 #         ans -= blk - v[i][0] + 1

 #     if prev_blk != -1:
 #         t = prev_blk - v[i][0]
 #         t_1 = prev_blk - cnted_i + 1
 #         if cnted_i < prev_blk and v[i][1] == 1:
 #             ans += 1
 #         # if v[i][1] == 1:
 #         #     ans += blk - v[i][0]+1
 #         ans += t * (t + 1) // 2 - t_1 * (t_1 + 1) // 2
 #         cnted_i = v[i][0]+1
 # if cnted_i < prev_blk and v[i][1] == 1:
 #     ans += 1
 # t = blk + 1
 # t_1 = blk - cnted_i + 1
 # ans += t * (t + 1) // 2 - t_1 * (t_1 + 1) // 2

n -= len(dic)
ans += n*m*(m+1)//2
# temp = [[0 for _ in range(m)] for _ in range(n)]
# ans = 0
# for j in range(n):
#     prev_w = -1
#     blk = m-1
#     for i in range(m-1, -1, -1):
#         if mat[j][i] == 2:
#             blk = i
#             prev_w = -1
#         elif mat[j][i] == 1:
#             if prev_w != -1:
#                 blk = prev_w
#             prev_w = i
#         else:
#             ans += blk-i+1
#             temp[j][i] = blk-i+1
print(ans)
# print(temp)

