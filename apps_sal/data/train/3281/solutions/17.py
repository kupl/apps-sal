import calendar


def unlucky_days(year):
    answer = 0

    for month in range(1, 13):
        for day in calendar.Calendar().itermonthdays2(year, month):
            if day[0] == 13 and day[1] == 4:
                answer += 1

    return answer

