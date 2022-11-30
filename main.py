def remove_comments(file_name):
    file = open(file_name,"r").read()
    content = ""
    index = 0
    flag = 0

    #clear comments ** **
    while index < len(file)-1:
        if(file[index] == "*" and file[index+1] == "*"):
            flag += 1
            index += 2
        elif flag % 2 == 1:  
            index += 1
        elif flag % 2 == 0:
            content += file[index]
            index += 1
    print(content)

remove_comments("test.txt")
#content = readFile.readline().strip()
#print(content)

#writeFile = open("newTest.txt","w")