def evaporator(content, evap_per_day, threshold):
    new_content = content
    for x in range(1,1000):
        new_content = new_content- new_content*(evap_per_day/100)
        if new_content < content*threshold/100:
            return x
