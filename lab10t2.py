csvFileName = input("Please enter csv file name: ")
csvFile = open(csvFileName + ".csv", "r")
for line in csvFile:
    print(line.replace("\n", "").split(","))

csvFile.close()
