# script para limpeza single-quotes no arquivo CSV
# dataset usado para teste: Summary information and metrics for Airbnb listings in Amsterdam
# source: http://insideairbnb.com/get-the-data.html
# not working as intend yet...

import csv

with open('summarized listings.csv', 'r') as csvfile:  # open original CSV file
    with open('edited summarized listings.csv', 'wb') as csvwriter:  # create new CSV file
        file = csv.reader(csvfile)
        writer = csv.writer(csvwriter)

        for line in file:
            newLine = line
            newLine[1] = newLine[1].replace("'", "")
            # newLine[1] = newLine[1].replace("\"\"", "")
            writer.writerow(newLine)
            # print writerLine[1]  # teste

    csvwriter.close()
csvfile.close()
