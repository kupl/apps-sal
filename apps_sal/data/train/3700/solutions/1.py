def kooka_counter(laughing):
    return 0 if laughing == '' else laughing.count('Hah') + laughing.count('haH') + 1
