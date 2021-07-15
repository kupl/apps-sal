def get_strings(city):
    dic = {} 
    for chr in city.lower():
        if chr.isalpha():
            dic[chr]=dic.get(chr,'')+'*'
    return ','.join([i+':'+dic[i] for i in dic])
