def what_time_is_it(a): return f'{str(int(a//30) or 12).zfill(2)}:{str(int((a-(30*(a//30)))//0.5)).zfill(2)}'
