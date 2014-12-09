#Calculate Flesch-Kincaid reading level for each project Description
#Will be later used to see if there is a difference in description reading level between high/low poverty schools
#Uses Python TextStat Module pypi.python.org/pypi/textstat/0.1.4

import csv
import sys
import string
from textstat.textstat import textstat

#Handle Large .CSV Files
int = sys.maxint
csv.field_size_limit(int)

inFile = "C:/Data/TextMining/Project/Merged CSV/mergedFullWithSentiment.csv"
outFile = "C:/Data/TextMining/Project/ReadingLevelFull.csv"

#location of full .csv
with open(inFile,"rb") as source:
        rdr= csv.reader( source, delimiter = ',' )

        #change path below to update output file location
        with open(outfile,"wb") as result:
            wtr= csv.writer( result, delimiter=',')
            i = 0
            for r in rdr:
                #get the description from each field
                description = r[2]

                #try/catch to calculate grade level
                try:
                    gradeLevel= textstat.flesch_kincaid_grade(description)
                except:
                    gradeLevel = 'Unable to calculate!'
                
                #append grade level calculation to list
                r.append(gradeLevel)
                wtr.writerow(r)
                i+=1

                #print obs to track execution in console
                print(i)


                            
                


 