for _ in range(int(input())):
 n = int(input())
 listt1 = [int(e) for e in input().split()]
 listt2 = [int(e) for e in input().split()]
 m = min(min(listt1), min(listt2))
 dic = {}
 flag, flag2 = True, True
 for e in listt1:
  if e not in dic:
   dic[e] = 1
  else:
   dic[e] += 1
 for e in listt2:
  if e not in dic:
   dic[e] = 1
  else:
   dic[e] += 1
 for e in dic:
  if dic[e] % 2 == 1:
   flag = False
 dic2 = {}
 listt1.sort()
 listt2.sort()
 for e in dic:
  if dic[e] % 2:
   flag2 = False
   break
  else:
   dic2[e] = dic[e] // 2
 if flag2 == 0:
  print(-1)
  continue
 ref = dic2.copy()

 listt11 = []
 listt22 = []
 for i in range(0, n):
  if ref[listt1[i]]:
   ref[listt1[i]] -= 1
  else:
   listt11.append(listt1[i])
 ref = dic2.copy()
 for i in range(0, n):
  if ref[listt2[i]]:
   ref[listt2[i]] -= 1
  else:
   listt22.append(listt2[i])
 if len(listt11) == 0:
  print(0)
  continue
 if len(listt11) != len(listt22):
  print(-1)
  continue
 final_value = 0
 listt11.sort()
 listt22.sort(reverse=True)
 for i in range(0, len(listt11)):
  final_value += min(2 * m, min(listt11[i], listt22[i]))
 print(final_value)
