import quandl
quandl.read_key()
bsesensex = list(quandl.get("BSE/SPBSS5IP", returns="numpy"))
openval = []
for i in range(len(bsesensex)):
    openval.append(bsesensex[i][1])
print(len(openval))
print(openval)
