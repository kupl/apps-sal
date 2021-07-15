sea_sick=lambda s: ["No Problem","Throw Up"][(s.count("~_")+s.count("_~"))/float(len(s))>0.2]
