import numpy as np
for _ in range(int(input())):
   n = int(input())-1;soldiers = [int(j) for j in input().split()]
   force = int(input());attacks = np.zeros(2*n,dtype=int);attacks[:n] = np.array(soldiers);attacks[n:2*n] = attacks[:n];shield = [0 for _ in range(n)];pow_of_2 = 1
   while n // pow_of_2 > 0:      pow_of_2 *= 2
   soldier_of_attack = (2 * n - pow_of_2) % n;pow_of_2 = attacks[soldier_of_attack] > force
   
   for i in range(n):
      if attacks[i] > force:         shield[i] = 10 ** 11
      elif n == 1:         shield[i] = force
      elif pow_of_2:
         shield[i] = force;         num_of_survivors = n;  soldiers = list(attacks[i:i+n]);         starting_soldier = (n - i) % n
         if (num_of_survivors - starting_soldier) % 2 == 1:            shield[i] += soldiers[-1]
         soldiers = [soldiers[i] for i in range(num_of_survivors) if i < starting_soldier or (i - starting_soldier) % 2 == 0];num_of_survivors = starting_soldier + (num_of_survivors - starting_soldier - 1) // 2
         if num_of_survivors > 1:
            pow_2 = 1
            while True:
               attacker = num_of_survivors - (num_of_survivors % pow_2);   pow_2 *= 2
               if attacker == 0:                  break
               if attacker % pow_2 == 0:                  shield[i] += soldiers[attacker]
      elif i == soldier_of_attack:         shield[i] = force
      else:         shield[i] = force + 1   
   shield_needed = min(shield)
   if shield_needed == 10 ** 11:      print("impossible")
   else:
      print("possible")
      for i in range(n):
         if shield[i] == shield_needed:print(str(i+1) + " " + str(shield_needed));break
