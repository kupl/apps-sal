#!/usr/bin/env python
from collections import Counter

sweets_number = int(input())
sweets_types = list(map(int, input().split()))
sweets_types_frequencies = Counter(sweets_types)
days = sum((count + 1) // 2 for count in list(sweets_types_frequencies.values()))
print(days)

