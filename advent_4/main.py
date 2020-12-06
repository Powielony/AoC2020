import re

file = open('input', 'r')

eclTupl = ('amb', 'blu', 'brn', 'gry', 'hzl', 'oth')

dane = list()
Valid = 0

for line in file:
    if line != "\n":
        dane += line.split()

        if len(dane) >= 7:
            
            slow = {'byr':"",'iyr':'','eyr':'','hgt':'','hcl':'','ecl':'','pid':''}

            for val in dane:
                valKey, valVal = val.split(':')
                slow[valKey] = valVal

            hclSearch = re.search("#", slow['hcl'])

            if int(eval(slow['byr'])) not in range(1920, 2002):
                break
            
            '''if slow['ecl'] not in eclTupl:
                break

            if int(eval(slow['eyr'])) not in range(2020, 2030):
                break
            
            if len(hclSearch.string) < 7:
                print(hclSearch.string)
                break'''

            Valid += 1
        
        

    else:
        dane = list()
        e = 0
        slow = dict()
        

print(Valid)
