def bits_battle(a):
  odds, evens = sum([bin(i).count('1') for i in a if i % 2]), sum([bin(i).count('0') - 1 for i in a if i % 2 == 0])
  return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'
