mod=12345787
memo=[0,8,95,1183,14824]
for i in range(10**5): memo.append((15*memo[-1]-32*memo[-2]+15*memo[-3]-memo[-4])%mod);
def five_by_2n(n): return memo[n]
