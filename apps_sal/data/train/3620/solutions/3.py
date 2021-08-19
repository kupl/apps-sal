from datetime import datetime
data = '\nAries March 21 April 19\nTaurus April 20 May 20\nGemini May 21 June 20\nCancer June 21 July 22\nLeo July 23 August 22\nVirgo August 23 September 22\nLibra September 23 October 22\nScorpio October 23 November 21\nSagittarius November 22 December 21\nCapricorn December 22 January 19\nAquarius January 20 February 18\nPisces February 19 March 20\n'
data = [line.split() for line in data.split('\n') if line.strip()]


def month(s):
    return datetime.strptime(s, '%B').month


data = [(z, month(m1), int(d1), month(m2), int(d2)) for (z, m1, d1, m2, d2) in data]


def get_zodiac_sign(day, month):
    for (z, m1, d1, m2, d2) in data:
        if m1 == month and d1 <= day or (m2 == month and day <= d2):
            return z
