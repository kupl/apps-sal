t = int(input())
for i in range(t):
 s = input()
 if len(s) == 0 or len(s) == 1:
  print("NO")
 else:
  if len(s)%2==0:
   flag = False
   half = int(len(s)/2)
   if s[0:half]== s[half:len(s)]:
    flag = True
   else:
    pass
  else:
   flag = False
   for j in range(len(s)):
    news = s[0:j]+s[j+1:len(s)]
    half = int(len(news) / 2)
    if news[0:half] == news[half:len(news)]:
     flag = True
     break
    else:
     continue
  if flag:
   print("YES")
  else:
   print("NO")
