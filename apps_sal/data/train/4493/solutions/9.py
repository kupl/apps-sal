def get_last_digit(index):
    ds = '011235831459437077415617853819099875279651673033695493257291'
    return int(ds[index % len(ds)])
