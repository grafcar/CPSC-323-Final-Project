rows, cols = (7, 9)
parsingTable = [["none" for i in range(cols)] for j in range(rows)]

parsingTable[0][0] = "aW" 
parsingTable[1][7] = "=E"
parsingTable[2][0] = "TQ"
parsingTable[2][5] = "TQ"
parsingTable[3][1] = "+TQ"
parsingTable[3][2] = "-TQ"
parsingTable[3][6] = "Lambda"
parsingTable[3][8] = "Lambda"
parsingTable[4][0] = "FR"
parsingTable[4][5] = "FR"
parsingTable[5][1] = "Lambda"
parsingTable[5][2] = "Lambda"
parsingTable[5][3] = "*FR"
parsingTable[5][4] = "/FR"
parsingTable[5][6] = "Lambda"
parsingTable[5][8] = "Lambda"
parsingTable[6][0]= "a"
parsingTable[6][5] = "(E)"

stack = []
input = "a=a*(a-a)$"

columns =["a","+","-","*","/","(",")","=","$"]

rows = ["S","W","E","Q","T","R","F"]

def read (str):
    str = str[1:]
    return str

stack.append("$")
stack.append("E")
varPop = stack.pop()