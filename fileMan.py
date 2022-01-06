from data import genRandData
        

def saveDataIntoFile(arr, fileName, head=None):
    res=""
    fLine=True
    for element in arr:
        if fLine:
            res=res+str(element)
            fLine=False
        else:
            res=res+"\n"+str(element)

    with open(fileName, "w") as f:
        if head!=None:
            f.write(head+"\n"+res)
        else:
            f.write(res)

def readDataFromFile(filename, head=False):
    arr=[]
    with open(filename,"r") as f:
        for line in f:
            arr.append(line)
    if head:
        arr.pop(0)
    return arr

def toFloat(element):
    try:
        x=float(element)
    except: 
        print("ERROR!")
    else:
        return x

def toFloatArr(arr):
    newArr=[]
    for element in arr:
        newArr.append(toFloat(element))
    return newArr


def toStrArr(arr):
    newArr=[]
    for element in arr:
        newArr.append(str(element))
    return newArr

arr=toFloatArr(readDataFromFile("PRUEBA.txt",True))
print(arr)


