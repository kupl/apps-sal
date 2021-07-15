n, l, r, Ql, Qr = [int(x) for x in input().split(' ')]
w = [int(x) for x in input().split(' ')];
sum = [0 for x in range(n+1)];
for i in range(1, n+1):
	sum[i] = sum[i-1] + w[i-1];
ans = 2**32;
for k in range(0, n+1):
	temp = sum[k]*l + (sum[n] - sum[k])*r;
	if (2*k > n):
		temp += (2*k-n-1)*Ql;
	elif (2*k < n):
		temp += (n-2*k-1)*Qr;
	ans = min(ans, temp);
print(ans);
