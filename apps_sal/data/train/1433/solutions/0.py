
t = int(input())

for i in range(0,t):
	a = input()
	b = input()
	
	agts=bgts=afour=bfour=aseven=bseven=altf=bltf=afts=bfts=0;
	
	for j in a:
		if j >= '7':
			if j > '7':
				agts += 1
			else:
				aseven += 1
		elif j >= '4':
			if j > '4':
				afts += 1
			else:
				afour += 1
		else:
			altf += 1
	
	for j in b:
		if j >= '7':
			if j > '7':
				bgts += 1
			else:
				bseven += 1
		elif j >= '4':
			if j > '4':
				bfts += 1
			else:
				bfour += 1
		else:
			bltf += 1
		
	nseven = 0
	nfour = 0
	
	if aseven > bfts:
		aseven -= bfts;
		nseven += bfts;
		bfts = 0;
	else:
		bfts -= aseven;
		nseven += aseven;
		aseven = 0;
	
	if bseven > afts:
		bseven -= afts;
		nseven += afts;
		afts = 0;
	else:
		afts -= bseven;
		nseven += bseven;
		bseven = 0;
	
	if aseven > bltf:
		aseven -= bltf;
		nseven += bltf;
		bltf = 0;
	else:
		bltf -= aseven;
		nseven += aseven;
		aseven = 0;
	
	if bseven > altf:
		bseven -= altf;
		nseven += altf;
		altf = 0;
	else:
		altf -= bseven;
		nseven += bseven;
		bseven = 0;
	
	if aseven > bfour:
		aseven -= bfour;
		nseven += bfour;
		bfour = 0;
	else:
		bfour -= aseven;
		nseven += aseven;
		aseven = 0;
	
	if bseven > afour:
		bseven -= afour;
		nseven += afour;
		afour = 0;
	else:
		afour -= bseven;
		nseven += bseven;
		bseven = 0;
	
	nseven += min(aseven,bseven)
	
	if afour > bltf:
		afour -= bltf;
		nfour += bltf;
		bltf = 0
	else:
		bltf -= afour;
		nfour += afour;
		afour = 0;
	
	if bfour > altf:
		bfour -= altf;
		nfour += altf;
		altf = 0
	else:
		altf -= bfour;
		nfour += bfour;
		bfour = 0;
	
	nfour += min(afour,bfour)
	
	print('7'*nseven + '4'*nfour)
