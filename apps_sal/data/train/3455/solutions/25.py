def disarium_number(n): return ['Not !!', 'Disarium !!'][sum(int(str(n)[i])**(i + 1) for i in range(len(str(n)))) == n]
