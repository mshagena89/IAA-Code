#This script uses Dr. Healy's ANEW module to calculate Sentiment on Project Description Fields
#See more at csc.ncsu.edu/faculty/healey/maa-14/text/

import anew
import sys
import csv
import string

inputFile = "C:\Data\TextMining\Project\Merged CSV\mergedFull.csv"
outputFile = "C:\Data\TextMining\Project\sentimentTest.csv"

#required to work with large .csv File
#See stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
int = sys.maxint
csv.field_size_limit(int)

def AddSentimentToFile(inputFile, outputFile):
    with open(inputFile,"rb") as source:
            rdr= csv.reader( source )

            #change path below to update output file location
            with open(outputFile,"wb") as result:
                wtr= csv.writer( result )
                i = 0
                for r in rdr:
                    #Parse out Description from Source Document field 
                    descriptionSentiment = r[2]
                    descList = string.split(descriptionSentiment)
                
                    #Get the sentiment for all terms in project description field
                    results = anew.sentiment(descList)

                    #append the new arousal and valence calculations to input document
                    r.append(str(results['arousal']))
                    r.append(str(results['valence']))
                    wtr.writerow(r)

                    i+=1

#Add valence and arousal fields to each existing record in project list source file
AddSentimentToFile(inputFile, outputFile)
