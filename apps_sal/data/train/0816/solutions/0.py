def bookList():
    numBooks=int(input())
    bookNum=[int(x) for x in input().split()]
    takenBooks=int(input())
    for i in range(takenBooks):
        takenBookPos=(int(input()))
        a=bookNum[takenBookPos-1]
        print(a)
        bookNum.remove(a)

bookList()

