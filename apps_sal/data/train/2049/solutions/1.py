def sumBin(a, b, varMap):
  lhs = varMap[a]
  rhs = varMap[b]
  return bin(int(lhs, 2) + int(rhs, 2))[2:]

def andBin(a, b, varMap):
  lhs = varMap[a]
  rhs = varMap[b]
  return bin(int(lhs, 2) & int(rhs, 2))[2:]

def orBin(a, b, varMap):
  lhs = varMap[a]
  rhs = varMap[b]
  return bin(int(lhs, 2) | int(rhs, 2))[2:]

def xorBin(a, b, varMap):
  lhs = varMap[a]
  rhs = varMap[b]
  return bin(int(lhs, 2) ^ int(rhs, 2))[2:]

mapOper = {'AND': andBin, 'OR': orBin, 'XOR' : xorBin}


n, m = list(map(int, input().split()))
minMap = {"?": "0", "": "0"}
maxMap = {"?": "1"*m, "": "0"}

minSum = "0"
maxSum = "0"
for _ in range(n):
  name, _, expr = input().split(' ', 2)

  if len(expr.split(' ')) == 1:
    minMap[name] = expr
    maxMap[name] = expr
  else:
    lhs, oper, rhs = expr.split()
    minMap[name] = mapOper[oper](lhs, rhs, minMap).zfill(m)
    maxMap[name] = mapOper[oper](lhs, rhs, maxMap).zfill(m)

  minSum = sumBin("", name, minMap)
  maxSum = sumBin("", name, maxMap)


def countOnes(i, varMap):
  ones = 0
  for name, num in list(varMap.items()):
    if name != "?" and name != "":
      ones += num[i] == "1"
  return ones

minRes = ""
maxRes = ""

for i in range(m):
  zeroOnes = countOnes(i, minMap)
  oneOnes = countOnes(i, maxMap)

  if zeroOnes > oneOnes:
    maxRes += "0"
    minRes += "1"
  elif zeroOnes < oneOnes:
    maxRes += "1"
    minRes += "0"
  else:
    maxRes += "0"
    minRes += "0"

print (minRes)
print (maxRes)


