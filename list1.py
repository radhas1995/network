def match_ends(words):
    count = 0
    for char in words:
        if len(char)>2 and char[0:2]==char[len(char)-2:]:
            count = count+1
    return (count)
print (match_ends(["radra",'tannu','by', 'and']))
