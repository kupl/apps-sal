from datetime import timedelta


def solve(arr):
    max = 0
    a = list(dict.fromkeys(arr))
    new_list = []
    if len(a) > 1:
        for i in enumerate(a):
            new_list.append(str(i[1].replace(':', '')))
        new_list.sort()
        new_list.reverse()
        for i in enumerate(new_list):
            if i[0] <= len(new_list) - 2:
                delta_hours = int(i[1][:2]) - int(new_list[i[0] + 1][:2])
                delta_mins = int(i[1][2:]) - int(new_list[i[0] + 1][2:]) - 1
                t = str(timedelta(hours=delta_hours, minutes=delta_mins))[:-3]
                c = int(t.replace(':', ''))
                if c >= max:
                    max = c
                    result = t
            if i[0] == len(new_list) - 1:
                loop_hrs = int(i[1][:2]) - int(new_list[0][:2]) + 24
                loop_mins = int(i[1][2:]) - int(new_list[0][2:]) - 1
                d = str(timedelta(hours=loop_hrs, minutes=loop_mins))[:-3]
                c = int(d.replace(':', ''))
                if c >= max:
                    result = d
        if len(result) == 4:
            result = '0' + result
        return result
    else:
        return '23:59'
