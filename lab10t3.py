def generateDictionary ():
    textFile = open("font3.txt")
    dic={}
    for line in textFile:
        textFilelist = line.replace("\n","").split(",")
        dic[textFilelist[1]] = textFilelist[0]

    textFile.close()
    return dic

dictionary = generateDictionary()
print(dictionary)


bika = input("enter a character")
if bika in dictionary:
    print(dictionary[bika])
else:
    print("whatever")