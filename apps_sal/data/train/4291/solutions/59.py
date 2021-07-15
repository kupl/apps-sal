
def century(year):
    sonuc=0
    if (year%100 == 0):
        sonuc=year/100
    else:
        sonuc=(year/100)+1
    
    return int(sonuc);
