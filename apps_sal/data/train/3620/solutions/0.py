def get_zodiac_sign(day, month):

    signs = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer",
             "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]

    limits = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]

    return signs[month - 1] if limits[month - 1] <= day else signs[(month + 10) % 12]
