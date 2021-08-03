def uncollapse(s): return __import__('re').sub('(zero|one|two|three|four|five|six|seven|eight|nine)', r' \1', s)[1:]
