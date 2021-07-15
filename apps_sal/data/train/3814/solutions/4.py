def get_military_time(s):
    return "%02d:%02d:%02d" % (int(s[:2]) % 12 + 12 * (s[-2] != 'A'), int(s[3:5]), int(s[6:8]))
