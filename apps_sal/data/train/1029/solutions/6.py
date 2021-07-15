for _ in range(int(input())):
 n,m = map(int,input().split())
 list1 = list(map(int,input().split()))
 list1.sort()
 list2 = [i for i in range(1,n+1) if not i in list1]
 list2.sort()
 cheflist = [list2[i] for i in range(len(list2)) if i%2 == 0]
 asslist = [list2[i] for i in range(len(list2)) if i%2 != 0]
 str1 = ""
 str2 = ""
 for i in cheflist:
  if i == cheflist[len(cheflist)-1]:
   str1 += str(i)

  else:
   str1 += str(i) + " "

 for i in asslist:
  if i == cheflist[len(cheflist)-1]:
   str2 += str(i)

  else:
   str2 += str(i) + " "

 print(str1)
 print(str2)
