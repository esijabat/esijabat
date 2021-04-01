myUniqueList = []


def AddList(a):
    myUniqueList.append(a)
    if a in myUniqueList:
        return True
    else:
        return False


UpdatedList = AddList(2)
UpdatedList = AddList(3)
UpdatedList = AddList(10)

print(myUniqueList)
