def bits_battle(numbers):
  odds, evens = sum(bin(n).count("1") for n in numbers if n%2), sum(bin(n).count("0")-1 for n in numbers if not n%2)
  return ["odds win", "evens win"][odds - evens < 0] if odds - evens else "tie"
