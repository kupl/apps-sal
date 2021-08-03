def what_century(year):
    year = str(year)
    st = year[:2]
    st = int(st)
    gt = st + 1
    gt = str(gt)
    if year != "0000" and year[1:] != "000" and year[2:] != "00":
        if len(gt) == 2:
            if (gt[0] == "1") and (gt[1] == "0"):
                return("10th")
            elif (gt[0] == "1") and (gt[1] in range(1, 10)):
                return(f"{gt}th")
            elif gt[0] != "1" and gt[1] == "0":
                return(f"{gt}th")
            elif gt[0] != "1" and gt[1] == "1":
                return(f"{gt}st")
            elif gt[0] != "1" and gt[1] == "2":
                return(f"{gt}nd")
            elif gt[0] != "1" and gt[1] == "3":
                return(f"{gt}rd")
            else:
                return(f"{gt}th")
        else:
            if gt[0] == 1:
                return("1st")
            elif gt[0] == 2:
                return("2nd")
            elif gt[0] == 3:
                return("3rd")
            else:
                return(f"{gt}th")
    elif year[1:] == "000" and year != "0000":
        return(f"{year[0]}0th")
    elif year[2:] == "00" and year[1:] != "000" and year != "0000":
        if year[1] == "1":
            return(f"{year[:2]}st")
        elif year[2] == "2":
            return(f"{year[:2]}nd")
        elif year[2] == "3":
            return(f"{year[:2]}rd")
        else:
            return(f"{year[:2]}th")
    elif year == "0000":
        return("0th")
