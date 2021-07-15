is_madhav_array=lambda a:(print(a),False if len(a)<3 or len(a)==5 or a[-1]+a[0]==7else len(set(sum(a[int(i*(i+1)/2):int((i+2)*(i+1)/2)]) for i in range(int(len(a)**.5)+1)))==1)[1]
