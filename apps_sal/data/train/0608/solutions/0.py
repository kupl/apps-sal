for i in range(int(input())):
	 n = int(input())
	 P = list(map(float, input().split()))
	 pr = 1
	 for p in P:
		  a = 100+p
		  pr = (pr*a)/100
	 pr = (pr-1)*100
	 x = 6-len(str(int(abs(pr))))
   	 if (x==1):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.1f" % round(pr,x)))
		 else:
		 	print(str("%.1f" % round(pr,x)))
	 elif (x==2):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.2f" % round(pr,x)))
		 else:
		 	print(str("%.2f" % round(pr,x)))
	 elif (x==3):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.3f" % round(pr,x)))
		 else:
		 	print(str("%.3f" % round(pr,x)))
	 elif (x==4):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.4f" % round(pr,x)))
		 else:
		 	print(str("%.4f" % round(pr,x)))
	 elif (x==5):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.5f" % round(pr,x)))
		 else:
		 	print(str("%.5f" % round(pr,x)))
	 elif (x==6):
   	 	 if (pr==0):
   	 	 	print(0)
		 elif (pr>0):
		 	print("+"+str("%.6f" % round(pr,x)))
		 else:
		 	print(str("%.6f" % round(pr,x)))
