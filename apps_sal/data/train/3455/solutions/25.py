disarium_number=lambda n:['Not !!','Disarium !!'][sum(int(str(n)[i])**(i+1) for i in range(len(str(n))))==n]
