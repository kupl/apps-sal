for _ in range(int(input())):
 s = input()
 arr =[]
 for i in range(len(s)):
  if s[i] in arr:
   pass
  else:
   arr.append(s[i])
 print(len(arr))

