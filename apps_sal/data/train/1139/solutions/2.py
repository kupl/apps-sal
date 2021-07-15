def numDecodings(s):
 s = '10' + s
 dec = [1] * (len(s) + 2)

 for i in range(2, len(s)):
  # invalid case or '10, 20'
  if s[i] == '0':
   if s[i - 1] != '1' and s[i - 1] != '2':
    return 0
   dec[i] = dec[i - 2]
  # 1 - 9, 27 -
  elif int(s[i - 1: i + 1]) > 26 or int(s[i - 1: i + 1]) < 10:
   dec[i] = dec[i - 1]
   # 11 - 26 (except for 20)
  else:
   dec[i] = dec[i - 1] + dec[i - 2]

 return dec[len(s) - 1]

for _ in range(int(input()))    :
 nums = input()
 ways = numDecodings(nums)
 print(["NO", "YES"][ ways % 2 == 0])
