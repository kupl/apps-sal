def weather_info(t): return (lambda c: '{} is{} freezing temperature'.format(c, ' above' if c >= 0 else ''))((t - 32) * 5 / 9.0)
