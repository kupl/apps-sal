def count_squares(img):
  h,w,r=len(img),max([len(s) for s in img]),0
  img=[s+" "*(w-len(s)) for s in img]
  for i in range(h): 
    for j in range(w):
      if img[i][j]=="+":
        for k in range(1,min(h-i,w-j)):
          if img[i+k][j+k]=="+" and img[i+k][j]=="+" and img[i][j+k]=="+":
            s1=img[i][j+1:j+k]+img[i+k][j+1:j+k]
            s2="".join([x[j] for x in img])[i+1:i+k]+"".join([x[j+k] for x in img])[i+1:i+k]
            if not (" " in s1+s2 or "|" in s1 or "-" in s2): r+=1
  return r
