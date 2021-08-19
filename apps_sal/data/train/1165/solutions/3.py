import datetime
month_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


def getHalfBirthday(date, month):
    half_year = datetime.timedelta(days=366 / 2)
    if month < 2:
        bday = datetime.date(2004, month + 1, date)
    else:
        bday = datetime.date(2003, month + 1, date)
    hbd = bday + half_year
    hbd = str(hbd.day) + ' ' + month_names[hbd.month - 1]
    return hbd


def main():
    t = int(input())
    for _ in range(t):
        (date, month) = input().split()
        date = int(date)
        month = month_names.index(month)
        answer = getHalfBirthday(date, month)
        print(answer)


main()
