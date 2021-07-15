for _ in range(int(input())):
 n, sm1, sm2, smf = int(input()), 0, 0, 0
 l1, l2 = list(map(int, input().split())), list(map(int, input().split()))
 for i in range(n):
  if sm1==sm2 and l1[i]==l2[i]: smf+=l1[i]
  sm1+=l1[i]; sm2+=l2[i]
 print(smf)
