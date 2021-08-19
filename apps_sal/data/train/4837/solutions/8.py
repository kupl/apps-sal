def parse(crontab):
    cron_list = crontab.split(' ')
    cron_ranges = ['0-59', '0-23', '1-31', '1-12', '0-6']
    weekdays = {'SUN': 0, 'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6}
    months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    for (i, r) in enumerate(cron_list):
        val_out = []
        for v in r.split(','):
            step = 1
            if '/' in v:
                step = int(v.split('/')[1])
                v = v.split('/')[0]
            if '-' in v:
                start = (months[v.split('-')[0]] if i == 3 else weekdays[v.split('-')[0]]) if not v.split('-')[0].isnumeric() else int(v.split('-')[0])
                stop = (months[v.split('-')[1]] + 1 if i == 3 else weekdays[v.split('-')[1]] + 1) if not v.split('-')[1].isnumeric() else int(v.split('-')[1]) + 1
                val_out += [i for i in range(start, stop, step)]
            elif '*' in v:
                start = int(cron_ranges[i].split('-')[0])
                stop = int(cron_ranges[i].split('-')[1]) + 1
                val_out += [i for i in range(start, stop, step)]
            else:
                val_out += [int(v)]
        cron_list[i] = ' '.join([str(i) for i in sorted(val_out)])
    return '{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}'.format('minute', cron_list[0], 'hour', cron_list[1], 'day of month', cron_list[2], 'month', cron_list[3], 'day of week', cron_list[4])
