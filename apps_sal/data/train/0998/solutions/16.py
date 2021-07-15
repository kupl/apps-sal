check_digit = lambda x: int(x) if x.isdigit() else x
n, q = map(int, input().split())
rows = {i : 0 for i in range(n)}
columns = {i : 0 for i in range(n)}

for _ in range(q):
 op, num, x = map(check_digit, input().split())
 if op == "RowAdd":
  rows[num-1] += x
 else:
  columns[num-1] += x
print(max(rows.values()) + max(columns.values()))
