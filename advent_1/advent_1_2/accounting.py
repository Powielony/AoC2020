file1 = open('input', 'r')




for val1 in file1:
    file2 = open('input', 'r')
    
    for val2 in file2:
        file3 = open('input', 'r')
        
        for val3 in file3:
            if(int(val1)+int(val2)+int(val3)==2020):
                print(int(val1)*int(val2)*int(val3))
            
        file3.close()
    file2.close()
file1.close()
