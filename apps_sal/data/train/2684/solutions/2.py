ones = {0:"Woda", 1:"Jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"piec", 6:"szesc" , 7:"siedem", 8:"osiem", 9:"dziewiec"}
twos = {10:"dziesiec", 11:"jedenascie", 12:"dwanascie", 13:"trzynascie", 14:"czternascie", 15:"pietnascie", 16:"szesnascie", 17:"siedemnascie", 18:"osiemnascie", 19:"dziewietnascie"}
tens = {10:"dziesiec", 20:"dwadziescia", 30:"trzydziesci", 40:"czterdziesci", 50:"piecdziesiat", 60:"szescdziesiat", 70:"siedemdziesiat", 80:"osiemdziesiat", 90:"dziewiecdziesiat"}

ordering_beers=lambda n:[ones.get(n,twos.get(n,tens.get(n,tens[(n//10or 1)*10]+' '+ones[n%10]))),'Jedno'][n==1].capitalize() + ' ' +\
                        ['mineralna',['piwo',['piw','piwa'][n in[2,3,4]or(n//10in[2,3,4]and n%10 in[2,3,4])]][n!=1]][n!=0] + ' ' +\
                        'poprosze'
