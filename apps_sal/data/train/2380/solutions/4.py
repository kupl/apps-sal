t = int(input())
while t > 0 :
	t -= 1
	n, k = map(int, input().split())
	s = input()
	cnt, v = [0] * k, [list() for i in range(k)]
	ans = 0
	for i in range(n) :
		if s[i] == '1' :
			cnt[i % k] += 1
			ans += 1
		v[i % k].append(int(s[i]))
	tot = ans
	for i in range(k) :
		curAns = tot - cnt[i]
		tot0, tot1 = 0, 0
		mnsum = 0
		for j in range(len(v[i])) :
			if v[i][j] == 0 :
				tot0 += 1
			else :
				tot1 += 1
			ans = min(ans, curAns + mnsum + tot0 + (cnt[i] - tot1))
			mnsum = min(mnsum, tot1 - tot0)

	print(ans)
