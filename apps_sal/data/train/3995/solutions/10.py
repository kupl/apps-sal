dating_range = lambda a: "{}-{}".format(int(a-0.1*a if a <= 14 else a/2+7), int(a+0.1*a if a <= 14 else (a-7)*2))
