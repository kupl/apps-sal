for _ in range(int(input())):
 n = int(input())
 arr = sorted(list(map(int, input().split())))
 a = n // 4
 b = a + a
 c = b + a
 if arr[a] == arr[a-1] or arr[b] == arr[b-1] or arr[c] == arr[c-1]:
  print(-1)
 else:
  print(arr[a], arr[b], arr[c])
