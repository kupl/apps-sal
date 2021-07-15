from datetime import datetime

data = """
Aries March 21 April 19
Taurus April 20 May 20
Gemini May 21 June 20
Cancer June 21 July 22
Leo July 23 August 22
Virgo August 23 September 22
Libra September 23 October 22
Scorpio October 23 November 21
Sagittarius November 22 December 21
Capricorn December 22 January 19
Aquarius January 20 February 18
Pisces February 19 March 20
"""
data = [line.split() for line in data.split('\n') if line.strip()]
month = lambda s: datetime.strptime(s, '%B').month
data = [(z, month(m1), int(d1), month(m2), int(d2)) for z, m1, d1, m2, d2 in data]

def get_zodiac_sign(day, month):
    for z, m1, d1, m2, d2 in data:
        if (m1 == month and d1 <= day) or (m2 == month and day <= d2):
            return z
