import csv
from call import name

with open('Nova_Scotia_Baby_Names.csv') as Nova_Scotia_Baby_Names:
    reader = csv.reader(Nova_Scotia_Baby_Names)
    NSYears = []
    frequencyFNS = {}
    frequencyMNS = {}
    for row in reader:
        if row[0] not in NSYears:
            NSYears.append(row[0])
        
        if row[1] == 'F' and row[2].title() == name:
            frequencyFNS[row[0]] = row[3]
        
        if row[1] == 'M' and row[2].title(  ) == name:
            frequencyMNS[row[0]] = row[3] 

NSYears.pop(0)

frequencyFNS0 = {}
frequencyMNS0 = {}

for year in NSYears:
    frequencyFNS0[year] = 0
    frequencyMNS0[year] = 0

for x in NSYears:
    for key, value in frequencyFNS.items():
        if key == x:
            frequencyFNS0[key] = int(value)

    
    for key, value in frequencyMNS.items():
        if key == x:
            frequencyMNS0[key] = int(value)

comboDict = {}
for key in frequencyFNS0.keys():
    comboDict[key] = []
    comboDict[key].append(frequencyFNS0[key])
    comboDict[key].append(frequencyMNS0[key])

NSYears = comboDict.keys()
NSFemale = [x[0] for x in comboDict.values()]
NSMale = [x[1] for x in comboDict.values()]