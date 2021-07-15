def past(h, m, s):
    hms, mms, sms = 3600000, 60000, 1000
    return h * hms + m * mms + s * sms
