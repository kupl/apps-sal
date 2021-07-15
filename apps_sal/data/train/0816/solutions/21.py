#https://www.codechef.com/IARCSJUD/problems/BOOKLIST

try:
    num_books = int(input())

    books = [int(x) for x in input().split()]

    borrows = int(input())

    for i in range(borrows):
    
        curbook_index = int(input()) - 1
        curbook = books.pop(curbook_index)
    
        print(curbook)

except:
    pass
