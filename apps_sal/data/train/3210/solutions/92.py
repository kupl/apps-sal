def get_strings(city):
    new_city = ''.join(filter(str.isalpha, city.lower()))
    char_seen=[]
    for char in new_city:
      if char not in char_seen:
        char_seen.append(char)

    count_char = []
    for char in char_seen:
      x =new_city.count(char)
      count_char.append(x)

    d = dict(zip(char_seen, count_char))

    total_str = []
    for char, count in d.items():
      count_str = char + ":" + count*"*"
      total_str.append(count_str)
    
    return ','.join(total_str)
