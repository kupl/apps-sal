import time
def fizz_buzz_cuckoo_clock(d):
        #print(d)
        d = time.strptime(d, '%H:%M')
        hour,sec = d.tm_hour, d.tm_min
        o = ''
        if sec == 0:
            if 1 <= hour <= 12:
                o = ('Cuckoo'+' ')*hour
            else:  # 13
                dic = {13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,00:12}
                o = ('Cuckoo'+' ')*dic[hour]
        else:
            if sec == 30:
                o ='Cuckoo'
            elif sec % 3 == 0 and sec % 5 == 0:
                o = 'Fizz Buzz'
            elif sec % 3 == 0:
                o= 'Fizz'
            elif sec % 5 == 0:
                o = 'Buzz'
            else:
                o = 'tick'

        return o.rstrip()


