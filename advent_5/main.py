file = open("input", "r")

rowid = ''
colid = ''
maxseatid = 0
currseatid = 0
seatidlist = []

for line in file:
    
    rowid = ''
    colid = ''
    
    for char in line:
        if char == "B":
            rowid += "1"
        if char == "F":
            rowid += "0"
        if char == "R":
            colid += "1"
        if char == "L":
            colid += "0"
        if char == '\n':
            power = 6
            for dig in rowid:
                currseatid += int(dig)*(pow(2, power))
                power -=1
            currseatid *= 8
            power = 2
            for dig in colid:
                currseatid += int(dig)*(pow(2, power))
                power -=1

            if currseatid > maxseatid:
                maxseatid = currseatid

            seatidlist.append(currseatid)

            rowid = ''
            colid = ''
            currseatid = 0


for i in range(8, 900):
    if i not in seatidlist:
        print(i)

print(maxseatid)

file.close()
