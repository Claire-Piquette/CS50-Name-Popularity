import csv
from call import name

# find the right string that matches the name in the female file
with open('BC_Female_Names.csv') as BC_Female:
    reader = csv.reader(BC_Female)
    BCYears = []
    frequencyFBC = ""
    for years in reader:
        BCYears = years
        BCYears.pop(0)
        BCYears.pop(len(years) - 1)
        break
    for row in reader:
        if row[0].title() == name:
            frequencyFBC = row

    # get rid of the first element since it is the name
if len(frequencyFBC) > 0:
    frequencyFBC.pop(0)

# find the right string that matches the name in the male file
with open('BC_Male_Names.csv') as BC_Male:
    reader = csv.reader(BC_Male)
    frequencyMBC = {}
    for row in reader:
        if row[0].title() == name:
            frequencyMBC = row

    # get rid of the first element since it is the name
if len(frequencyMBC) > 0 :            
    frequencyMBC.pop(0)

keys = []
for x in range(len(BCYears)):
    keys.append(int(x))

BCFemale = []
if len(frequencyFBC) > 0:
    for x in range(len(frequencyFBC) - 1):
        BCFemale.append(int(frequencyFBC[x]))

if len(frequencyFBC) == 0:
    for x in range(len(BCYears)):
        BCFemale.append(0)

BCMale = []
if len(frequencyMBC) > 0:
    for x in range(len(frequencyMBC) - 1):
        BCMale.append(int(frequencyMBC[x]))

if len(frequencyMBC) == 0:
    for x in range(len(BCYears)):
        BCMale.append(0)

BCFemaleDict = {}
for row in range(len(BCYears)):
    BCFemaleDict[BCYears[row]] = BCFemale[row]

BCMaleDict = {}
for row in range(len(BCYears)):
    BCMaleDict[BCYears[row]] = BCMale[row]

comboDict = {}
for key in BCYears:
    comboDict[key] = []
    comboDict[key].append(BCFemaleDict[key])
    comboDict[key].append(BCMaleDict[key])


BCYears = comboDict.keys()
BCFemale = [x[0] for x in comboDict.values()]
BCMale = [x[1] for x in comboDict.values()]