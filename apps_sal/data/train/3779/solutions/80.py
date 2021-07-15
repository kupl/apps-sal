def past(h, m, s):
    Hms = h*60*60*1000
    Mms = m*60*1000
    Sms = s*1000
    return Hms+Mms+Sms
