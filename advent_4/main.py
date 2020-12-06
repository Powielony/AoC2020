file = open('input', 'r')

data = ""
Valid = 0
numOfFields = 0
e = 0
r = 0

for line in file:
    if line != "\n":
        data += line
        dane = data.split()

        numOfFields = len(dane)

        if numOfFields >= 7:
            dane.sort()

            if numOfFields >= 8:
                dane.pop(
        

        
        

    else:
        dane = ""
        numOfFields = 0
        data = ""
        e = 0
        

print(Valid)
