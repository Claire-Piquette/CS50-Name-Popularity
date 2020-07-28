import csv
from call import name

with open('Alberta_Baby_Names.csv', encoding='utf-8') as Alberta_Baby_Names:
    reader = csv.reader(Alberta_Baby_Names)
    ALYears = []
    frequencyFAL = {}
    frequencyMAL = {}
    for row in reader:
        if row[4] not in ALYears:
            ALYears.append(row[4])

        if row[3] == 'Girl' and row[1] == name:
            frequencyFAL[row[4]] = row[2]

        if row[3] == 'Boy' and row[1] == name:
            frequencyMAL[row[4]] = row[2]

frequencyFAL0 = {}
frequencyMAL0 = {}

for year in ALYears:
    frequencyFAL0[year] = 0
    frequencyMAL0[year] = 0

for x in ALYears:
    for key, value in frequencyFAL.items(): 
        if key == x: 
            frequencyFAL0[key] = int(value)

    for key, value in frequencyMAL.items(): 
        if key == x: 
            frequencyMAL0[key] = int(value)

comboDict = {}
for key in frequencyFAL0.keys():
    comboDict[key] = []
    comboDict[key].append(frequencyFAL0[key])
    comboDict[key].append(frequencyMAL0[key])


AlbertaYears = comboDict.keys()
AlbertaFemale = [x[0] for x in comboDict.values()]
AlbertaMale = [x[1] for x in comboDict.values()]