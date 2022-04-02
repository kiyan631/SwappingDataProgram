def swapFileData():
    file1 = input("Enter the file name to be swiped :-")
    file2 = input("Enter the file name with which the contents to be swapped:-")


    a = open(file1, 'r')
    data_a= a.read()
    a.close()

    b = open(file2, 'r')
    data_b= b.read()
    b.close()

    with open(file2,'w') as a:  
     a.write(data_a)
   
    
     
    
    with open(file1,'w') as b :
        b.write(data_b)

    
    

   
    print('completed')


            
        
swapFileData()

