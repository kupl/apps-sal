
def main():
    n = int(input())
    home_aprt = str(input())
    balance = 0
    for i in range(n):
        f, s = input().split('->')
        if f == home_aprt:
            balance += 1
        else:
            balance -= 1

    if balance == 0:
        print('home')
    else:
        print('contest')


main()
