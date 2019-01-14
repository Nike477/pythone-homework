myUniqueList = []

num1 = 1
num2 = 2
num3 = 3
num4 = 4

def Numbers():
    if num1 not in myUniqueList:
        myUniqueList.append(num1)

    if num2 not in myUniqueList:
        myUniqueList.append(num2)

    if num3 not in myUniqueList:
        myUniqueList.append(num3)
        
    if num4 not in myUniqueList:
        myUniqueList.append(num4)
        print(myUniqueList)
        return True
    else:
        return False

Numbers()
