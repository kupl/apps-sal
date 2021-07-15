from re import sub, search

def generate_bc(url, separator):
  url = sub("https?:\/\/","", sub("\/index\..+$","",sub("[?#].+$","", url)))
  base = search(".+?\/", url).group(0) if search(".+?\/", url) else url
  #if (base==nil): return '<span class="active">HOME</span>'
  paths = url[len(base):].split("/")
  path = "/"
  breadcrumbedPath = ['<a href="/">HOME</a>']
  if (url==base): return '<span class="active">HOME</span>'
  classes = None; last = False
  for i in xrange(len(paths)):
      if i==len(paths)-1:
          classes='active'
          last=True
      path += paths[i] + "/"
      bcName = paths[i]
      if len(paths[i])>30: bcName=acronymize(bcName)
      bcName = parseName(bcName)
      breadcrumbedPath+=[createHTMLPath(bcName, path, classes, last)]
  return separator.join(breadcrumbedPath);

createHTMLPath=lambda bcName, url, classes, last: ''.join(['<a href="',url,'"',('' if classes==None else ''.join([' class="',classes,'"'])),'>',bcName,'</a>']) if not last else ''.join(['<span',('' if classes==None else ''.join([' class="',classes,'"'])),'>',bcName,'</span>'])

parseName=lambda bcName: sub("\.\w+","", " ".join(bcName.split("-"))).upper()

acronymize=lambda bcName: "".join([x[0] for x in bcName.lower().split("-") if x not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]])
