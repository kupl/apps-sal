n, operations = map(int, input().split())
rows = [0]*n
columns = [0]*n
maxi=-float("Inf")
for i in range(operations):
 temp =input().split()
 if temp[0]=="RowAdd":
  rows[int(temp[1])-1]+=int(temp[2])
 else:
  columns[int(temp[1])-1]+=int(temp[2])
  
print(max(rows)+max(columns))
