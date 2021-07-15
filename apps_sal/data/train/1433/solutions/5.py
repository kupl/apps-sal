
t = int(input())

a = []
b = []

for i in range(0,t):
	a = input()
	b = input()
	
	agts=bgts=afour=bfour=aseven=bseven=altf=bltf=afts=bfts=0;
	
	for j in a:
		if j >= '7':
			if j > '7':
				agts = agts + 1
			else:
				aseven = aseven + 1
		elif j >= '4':
			if j > '4':
				afts = afts + 1
			else:
				afour = afour + 1
		else:
			altf = altf + 1
	
	for j in b:
		if j >= '7':
			if j > '7':
				bgts = bgts + 1
			else:
				bseven = bseven + 1
		elif j >= '4':
			if j > '4':
				bfts = bfts + 1
			else:
				bfour = bfour + 1
		else:
			bltf = bltf + 1
		
	nseven = 0
	nfour = 0
	
	if aseven > bfts:
		aseven = aseven - bfts;
		nseven = nseven + bfts;
		bfts = 0;
	else:
		bfts = bfts - aseven;
		nseven = nseven + aseven;
		aseven = 0;
	
	if bseven > afts:
		bseven = bseven - afts;
		nseven = nseven + afts;
		afts = 0;
	else:
		afts = afts - bseven;
		nseven = nseven + bseven;
		bseven = 0;
	
	if aseven > bltf:
		aseven = aseven - bltf;
		nseven = nseven + bltf;
		bltf = 0;
	else:
		bltf = bltf - aseven;
		nseven = nseven + aseven;
		aseven = 0;
	
	if bseven > altf:
		bseven = bseven - altf;
		nseven = nseven + altf;
		altf = 0;
	else:
		altf = altf - bseven;
		nseven = nseven + bseven;
		bseven = 0;
	
	if aseven > bfour:
		aseven = aseven - bfour;
		nseven = nseven + bfour;
		bfour = 0;
	else:
		bfour = bfour - aseven;
		nseven = nseven + aseven;
		aseven = 0;
	
	if bseven > afour:
		bseven = bseven - afour;
		nseven = nseven + afour;
		afour = 0;
	else:
		afour = afour - bseven;
		nseven = nseven + bseven;
		bseven = 0;
	
	nseven = nseven + min(aseven,bseven)
	
	if afour > bltf:
		afour = afour - bltf;
		nfour = nfour + bltf;
		bltf = 0
	else:
		bltf = bltf - afour;
		nfour = nfour + afour;
		afour = 0;
	
	if bfour > altf:
		bfour = bfour - altf;
		nfour = nfour + altf;
		altf = 0
	else:
		altf = altf - bfour;
		nfour = nfour + bfour;
		bfour = 0;
	
	nfour = nfour + min(afour,bfour)
	
	print('7'*nseven + '4'*nfour)
