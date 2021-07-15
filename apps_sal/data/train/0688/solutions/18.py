for _ in range(int(input())):
 s = input()
 count = 0
 for i in range(8):
  count+= s[i] != s[i-1]
 print('uniform') if count <= 2 else print("non-uniform")
