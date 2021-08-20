(n, q) = (int(i) for i in input().split())
file_types = {}
for _ in range(n):
    (ext, mime) = input().split()
    file_types[ext] = mime
for _ in range(q):
    filename = input().strip()
    found = False
    for (ext, mime) in list(file_types.items()):
        if filename.endswith('.' + ext):
            print(mime)
            found = True
            break
    if not found:
        print('unknown')
