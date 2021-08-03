def decipher_this(string):
    words = string.split()
    res = []
    # check if there is a part only consisting digts
    for x in words:
        if x.isdigit():
            res.append(chr(int(x)))
    # if not then seperate the numbers and the string charakters in seperate variables
        elif len(x) >= 3:
            sum = ""
            new_str = ""
            for i in x:
                if i.isdigit():
                    sum += i
                else:
                    new_str += i
            # transverse the digit to the she specific letter and add the old string to it
            sum = chr(int(sum)) + new_str
            # ckeck if the string length has changed due to the transversation and switch the letter position
            if len(sum) > 2:
                x = (sum[0::len(sum) - 1] + sum[2:len(sum) - 1] + sum[1])
                res.append(x)
            else:
                res.append(sum)
    return " ".join(res)
