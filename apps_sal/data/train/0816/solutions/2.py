def solve():
    pass


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for i in range(m):
    book_pos = int(input())
    print(arr.pop(book_pos - 1))
