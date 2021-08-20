str = input()
ss = str.split()
xcr = None
xcxc = None
for wd in ss:
    if xcxc is None:
        xcr = len(wd)
        xcxc = wd
    elif len(wd) < xcr:
        xcr = len(wd)
        xcxc = wd
print(xcxc, end=' ')
for wd in ss:
    print(wd, xcxc, end=' ')
