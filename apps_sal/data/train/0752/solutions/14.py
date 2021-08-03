n, q = list(map(int, input().split()))

extensions = {}
for _ in range(n):
    ext_name, ext_type = input().split()
    extensions[ext_name] = ext_type

for _ in range(q):
    filename = input().strip()

    if '.' in filename:
        ext = filename.split('.')[-1]

        if extensions.get(ext) != None:
            print(extensions[ext])
        else:
            print("unknown")

    else:
        print("unknown")
