import sys
lineArray = sys.stdin.readline().rstrip()
testcases = int(lineArray)
counttestcase = 0
while counttestcase < testcases:
  friends = int(sys.stdin.readline().rstrip())
  lineArray = sys.stdin.readline().rstrip().split()
  length = int(lineArray[0])
  breadth = int(lineArray[1])
  for i in range(0,friends):
    if length == breadth:
      length = 0
      breadth = 0
      break
    if length < breadth:
      breadth = breadth - length
    else:
      length = length - breadth
  if length == 0 and breadth == 0:
    print("No")
  else:
    print("Yes", length*breadth)
  counttestcase = counttestcase + 1
