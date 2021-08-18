def decipher_this(string):
    words = string.split()
    res = []
    for x in words:
        if x.isdigit():
            res.append(chr(int(x)))
        elif len(x) >= 3:
            sum = ""
            new_str = ""
            for i in x:
                if i.isdigit():
                    sum += i
                else:
                    new_str += i
            sum = chr(int(sum)) + new_str
            if len(sum) > 2:
                x = (sum[0::len(sum) - 1] + sum[2:len(sum) - 1] + sum[1])
                res.append(x)
            else:
                res.append(sum)
    return " ".join(res)
