# cook your dish here
MOD = 1000000007

fact_mods = [0] * (501)
fact_mods[0], fact_mods[1] = 1, 1
for i in range(2, 501):
 fact_mods[i] = (fact_mods[i-1]*i) % MOD

for _ in range(int(input())):
 s = input()
 n = len(s)
 counts = {}
 denom = 1
 for ch in s:
  counts[ch] = counts.get(ch,0) + 1
 for ch in counts:
  denom = (denom * fact_mods[counts[ch]]) % MOD
 print(fact_mods[n]*pow(denom,MOD-2,MOD) % MOD)
 
 

