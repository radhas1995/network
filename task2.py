#first two and last two
def both_ends(s):
    if len(s)<=2:
        return ""
    else:
        a = s[0:2]+s[len(s)-2:]
        return a

print(both_ends("bannan"))
