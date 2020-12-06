f = open('input', 'r')




for val1 in f:
    g = open('input', 'r')
    for val2 in g:
        if(int(val1)+int(val2)==2020):
            print(int(val1)*int(val2))
    g.close()
    

f.close()
