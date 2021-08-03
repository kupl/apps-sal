n = int(input())
leng = 2 * n - 1
for row in range(0, leng):
    for col in range(0, leng):
        mini = row if row < col else col
        mini = mini if mini < leng - row else leng - row - 1
        mini = mini if mini < leng - col else leng - col - 1
        print(n - mini, end=" ")
    print("")
