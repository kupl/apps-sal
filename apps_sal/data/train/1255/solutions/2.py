letters = ['a']
for i in range(0, 25): letters.append(chr(ord(letters[i]) + 1))
for tests in range(int(input())):
 word = input().split();integer = int(word[1]);ret = ''
 for i in letters:
  if integer > 0: 
   ret += i
   if i in word[0]: integer -= 1
  else:
   if i not in word[0]: ret += i
  if len(ret) == len(word[0]): break
 print('NOPE') if len(ret) != len(word[0]) else print(ret)
