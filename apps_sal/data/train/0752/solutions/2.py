n, q = (int(i) for i in input().split())

file_types = {}
for _ in range(n):
 ext, mime = input().split()
 file_types[ext] = mime

for _ in range(q):
 filename = input().strip()

 if "." in filename:
  ext = filename.split(".")[-1]
  try:
   print(file_types[ext])
  except KeyError:
   print("unknown")
 else:
  print("unknown")
