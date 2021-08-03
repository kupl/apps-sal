def what_century(year):
    year = int(year)
    output_century = year // 100
    ordinal = ''

    if year % 100 > 0:
        output_century += 1

    if output_century > 10 and output_century < 14:
        ordinal = 'th'
    elif output_century % 10 == 1:
        ordinal = 'st'
    elif output_century % 10 == 2:
        ordinal = 'nd'
    elif output_century % 10 == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'

    return str(output_century) + ordinal
