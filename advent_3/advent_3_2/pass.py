file1 = open('input', 'r')

overall_counter = 0

for line in file1:
    data = line.split(' ')
    minim, maxim = data[0].split('-')
    minim = int(eval(minim))
    maxim = int(eval(maxim))
    letter = data[1][0]
    password = data[2]

    if ((password[minim-1] == letter) or (password[maxim-1]) == letter) and not ((password[minim-1] == letter) and (password[maxim-1]) == letter):
        overall_counter+=1
        

print(overall_counter)
