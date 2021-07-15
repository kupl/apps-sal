str1 = input()
ans = 0
for i,char1 in enumerate(str1):
	if char1 == 'A':
		count1 = 0
		count2 = 0
		for j in range(i):
			if (str1[j] == 'Q'):
				count1+= 1
		for j in range(i+1, len(str1)):
			if (str1[j] == 'Q'):
				count2+= 1
		ans += count1*count2
print(ans)
