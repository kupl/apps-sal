array_size = int(input())
arr = input().split(" ")
arr = list(map(int, arr))
query_no = int(input())
for tc in range(query_no):
    k = int(input())
    count = 0
    result = [[]]
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            sub = arr[i:j]
            result.append(sub)
    for i in result:
        if i != []:
            if k == (min(i)):
                count += 1
    print(count)
