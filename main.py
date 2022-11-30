import textwrap

def cleanup_file(file_name):
    file = open(file_name,"r").read()
    content, result = "","" #both values to store the data of the file
    index, flag = 0,0

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

    #removes the indent
    for line in content.splitlines():
        result += textwrap.dedent(line) + "\n"
    
    #removes all additional \n\n and whitespaces 
    for x in range(len(result.splitlines())):
        content = result.strip().replace("\n\n","\n")
        result = content.replace("  "," ")
        content = result
    return result

formated_file = cleanup_file("finalp1.txt")
new_file = open("finalp2.txt","w")
new_file.write(formated_file)
