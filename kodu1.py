def seosta_lapsed_ja_vanemad(a,b):
    f = open(a).read().split("\n")
    vanemad = open(b).read().split("\n")
    for element in f:
        for i in vanemad:
            print("sfas")

seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")