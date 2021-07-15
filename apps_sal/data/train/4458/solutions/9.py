def time_correct(t):
    if t == "":
        return ""
    
    from re import findall, VERBOSE
    
    try:
        time = findall("""\A
                            (\d{2}):
                            (\d{2}):
                            (\d{2})
                            \Z""", t, VERBOSE)

        hr,mn,sc = [int(x) for x in time[0]]
        
        mn += sc // 60
        sc %= 60
        hr += mn // 60
        mn %= 60
        hr %= 24
        
        return "{:02d}:{:02d}:{:02d}".format(hr, mn, sc)
    except:
        return None
