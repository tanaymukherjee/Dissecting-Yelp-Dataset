import csv, json, sys

# if you are not using utf-8 files, remove the next line
# set the encode to utf8
# sys.setdefaultencoding("UTF-8") 
# sys.setdefaultencoding(name)

# check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]

    # open json file
    # encoding="utf8"
    # errors='ignore'
    inputFile = open(fileInput, encoding="utf8")

    # load csv file
    outputFile = open(fileOutput, 'w')

    # load json content
    data = json.load(inputFile)

    # close the input file
    inputFile.close()

    # create a csv.write
    output = csv.writer(outputFile)

    # header row
    output.writerow(data[0].keys())

    # values row
    for row in data:
        output.writerow(row.values())