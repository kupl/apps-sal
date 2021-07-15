def get_zodiac_sign(day, month):
    SIGNS = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
    t = int(month)*100+int(day)
    com = [119,218,320,419,520,621,722,822,922,1023,1122,1222]
    for i in range(0, len(com)-1):
        if (t > com[i]) & (t <= com[i+1]):
            return SIGNS[i+1]
    return SIGNS[0]    
