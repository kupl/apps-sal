disarium_number = lambda n : ['Not !!', 'Disarium !!'][sum(int(d)**(i+1) for i, d in enumerate(str(n)))==n]
