unlucky_days = lambda y: len([m for m in range(1, 13) if __import__('datetime').date(y, m, 13).weekday() == 4])
