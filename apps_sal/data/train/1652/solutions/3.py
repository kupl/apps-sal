def format_duration(seconds):
    if seconds == 0:
        return 'now'
    (minu, sec) = divmod(seconds, 60)
    (hour, minu) = divmod(minu, 60)
    (day, hour) = divmod(hour, 24)
    (year, day) = divmod(day, 365)
    if year == 0:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 1:
                        return str(sec) + ' second'
                    return str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(minu) + ' minute'
                    if sec == 1:
                        return str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(minu) + ' minutes'
                    if sec == 1:
                        return str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(hour) + ' hour'
                    if sec == 1:
                        return str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(hour) + ' hours'
                    if sec == 1:
                        return str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day'
                    if sec == 1:
                        return str(day) + ' day and ' + str(sec) + ' second'
                    return str(day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' day and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days'
                    if sec == 1:
                        return str(day) + ' days and ' + str(sec) + ' second'
                    return str(day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(day) + ' days, ' + str(hour) + ' hours'
                if sec == 1:
                    return str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(day) + ' days and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
    if year == 1:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year'
                    if sec == 1:
                        return str(year) + ' year and ' + str(sec) + ' second'
                    return str(year) + ' year and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and  ' + str(hour) + ' hour'
                    if sec == 1:
                        return str(year) + ' year, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' year, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' year, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year and  ' + str(day) + ' day'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, and ' + str(day) + ' days'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours'
                if sec == 1:
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' year ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' year, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
    if year > 1:
        if day == 0:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years'
                    if sec == 1:
                        return str(year) + ' years and ' + str(sec) + ' second'
                    return str(year) + ' years and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and  ' + str(hour) + ' hour'
                    if sec == 1:
                        return str(year) + ' years, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' years, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' years, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day == 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years and  ' + str(day) + ' day'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' yeas, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes'
                if sec == 1:
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(day) + ' day, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' day, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
        if day > 1:
            if hour == 0:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, and ' + str(day) + ' days'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour == 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days and ' + str(hour) + ' hour and ' + str(sec)
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if sec == 0:
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours'
                if sec == 1:
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hour, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
            if hour > 1:
                if minu == 0:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days and ' + str(hour) + ' hours'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(sec) + ' seconds'
                if minu == 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minute'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minute and ' + str(sec) + ' seconds'
                if minu > 1:
                    if sec == 0:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours and ' + str(minu) + ' minutes'
                    if sec == 1:
                        return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' second'
                    return str(year) + ' years, ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minu) + ' minutes and ' + str(sec) + ' seconds'
