import quandl, pyperclip

quandl.ApiConfig.api_key = "dGS1yZ1R5pr4SyzYni-H"
quandl.read_key()
bsesensex = list(quandl.get("BSE/SPBSS5IP", returns="numpy"))
# bse = list(quandl.get("BSE/BOM539397", returns="numpy"))
lastn = int(input("Enter the number of last n days you want to take data for (0 for all) : "))
openval = []
if lastn != 0:
    for i in range(-1, -lastn - 1, -1):
        openval.append(bsesensex[i][1])
    openval = openval[::-1]
else:
    for i in range(len(bsesensex)):
        openval.append(bsesensex[i][1])

# openval2 = []
# for i in range(len(bse)):
#    openval2.append(bse[i][1])
# print(len(openval2))
# print(openval2)
pyperclip.copy(str(openval))
print('The array is already copied')
