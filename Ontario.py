import csv
from call import name

#iterate over database to find which datapoints correspond to desired name. Add year and frequency to corresponding dictionaries, list of year is included for the sake of 0
with open('Ontario_Female_Names.csv', errors= 'ignore') as Ontario_Female_Names:
    reader = csv.reader(Ontario_Female_Names)
    year = []
    frequencyFO = {}
    for row in reader:
        if row[0] not in year:
            year.append(row[0])
        if row[1].title() == name:
            frequencyFO[row[0]] = row[2]
year.pop(0)
year.pop(0)

with open('Ontario_Male_Names.csv', errors= 'ignore') as Ontario_Male_Names:
    reader = csv.reader(Ontario_Male_Names)
    frequencyMO = {}
    for row in reader:
        if row[1].title() == name:
            frequencyMO[row[0]] = row[2]

# creating the dictionaries of the data files, adding in the zeros
NamedictFO = {}
NamedictMO = {}
for x in year:
    NamedictFO[x] = 0
    NamedictMO[x] = 0

for x in year:
    for key, value in frequencyFO.items(): 
        if key == x: 
            NamedictFO[key] = int(value)

    for key, value in frequencyMO.items(): 
        if key == x: 
            NamedictMO[key] = int(value)

# create dictionary for graph
comboDict = {}
for key in NamedictFO.keys():
    comboDict[key] = []
    comboDict[key].append(NamedictFO[key])
    comboDict[key].append(NamedictMO[key])


OntarioYears = comboDict.keys()
OntarioFemale = [x[0] for x in comboDict.values()]
OntarioMale = [x[1] for x in comboDict.values()]