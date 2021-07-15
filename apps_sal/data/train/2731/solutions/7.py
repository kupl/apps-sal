day_and_time = lambda m: "{} {:02d}:{:02d}".format(["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][(m//1440)%7], (m//60)%24, m%60)
