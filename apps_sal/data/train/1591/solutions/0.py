arr = []
arr.append(1)
_ = 1
while _ <= 100002:
    arr.append(_ * arr[_ - 1] % 1589540031)
    _ += 1
for _ in range(int(input())):
    print(arr[int(input())])
