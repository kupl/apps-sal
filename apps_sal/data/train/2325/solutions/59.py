S = input()
T = input()
Q = int(input())

nS = [[0, 0]]
nT = [[0, 0]]

for i, c in enumerate(S):
  nS.append([abs(ord(c) - ord('A')), abs(ord(c) - ord('B'))])
  nS[i + 1][0] += nS[i][0]
  nS[i + 1][1] += nS[i][1]

for i, c in enumerate(T):
  nT.append([abs(ord(c) - ord('A')), abs(ord(c) - ord('B'))])
  nT[i + 1][0] += nT[i][0]
  nT[i + 1][1] += nT[i][1]

for qawsedrftgyhujikolp in range(Q):
  a, b, c, d = map(int, input().split())
  if (nS[b][0] - nS[a - 1][0] + 2 * nS[b][1] - 2 * nS[a - 1][1]) % 3 == (nT[d][0] - nT[c - 1][0] + 2 * nT[d][1] - 2 * nT[c - 1][1]) % 3:
    print("YES")
  else:
    print("NO")
