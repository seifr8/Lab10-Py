import csv
fileNames = ["2000_BoysNames","2000_GirlsNames"]
for fileName in fileNames:
    f = open(fileName + ".txt","r")
    namesCsv= open(fileName + ".csv","x", newline="")
    csvWriter = csv.writer(namesCsv)
    csvWriter.writerow(["first name", "count"])

    for line in f:
        line = line.replace("\n","")
        csvWriter.writerow(line.split(","))


    f.close()
    namesCsv.close()


