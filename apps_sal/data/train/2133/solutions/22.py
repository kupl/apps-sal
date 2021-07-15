print(max(map(lambda x: sum(map(int, x)), zip(*(list(input()) for i in range(int(input())))))))
