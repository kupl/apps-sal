for case in range(int(input())):
 num = int(input())
 list1 = list(map(int, input().split()))
 list2 = [list1[0]]
 for i in range(1, num):
  list2.append(list1[i] + list2[i - 1])
 # print(list2)
 know = 1
 day = 0
 while know < num:
  day += 1
  know += list2[know - 1]
 print(day)

