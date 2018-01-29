def fix_start(a):
    if a[0] in a[1:]:
        new = a[1:].replace(a[0],'*')
        print (a[0]+new)
fix_start("rare")

