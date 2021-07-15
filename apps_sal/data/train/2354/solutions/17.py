def solution():
	w = input().strip()
	n = int(input())
	words = []
	for i in range(n):
		words.append(input().strip())

	for i in range(n):
		if words[i] == w:
			return True
		for j in range(n):
			if words[i][1]+words[j][0] == w:
				return True
	
	return False


print('YES' if solution() else 'NO')
