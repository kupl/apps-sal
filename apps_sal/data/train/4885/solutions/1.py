find_gatecrashers=lambda p,i:sorted(set(p)-{elt for j,lst in i for elt in lst+[j] })
