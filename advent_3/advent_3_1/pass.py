file1 = open('input', 'r')

pos_counter = 0
tree_counter = 0
flag = 1

for line in file1:
    if flag == 1:
        if line[pos_counter] == '#':
            tree_counter += 1
        pos_counter+=1
        if pos_counter >=31:
            pos_counter -= 31
        flag -= 1
    else:
        flag = 1

print(tree_counter)
    
