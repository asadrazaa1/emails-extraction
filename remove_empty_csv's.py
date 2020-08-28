import psycopg2
import sys
from nltk.tokenize import sent_tokenize 
import re
import csv
import os



# pmid {16300001 - 16400000}

try:
#     starting_pmid = 16300001
#     intermediate_pmid = 16400000
    starting_pmid = 100001
    intermediate_pmid = 200000
    ending_pmid = 32078260

    while 1:
        if intermediate_pmid<ending_pmid:
            #open existing csv files
            with open('pmid {%s - %s}.csv' % (starting_pmid, intermediate_pmid), mode='r') as csv_file:
                reader = csv.reader(csv_file)

                if len(list(reader))==1:
                    #removing the file if there is only header in the file and there is no data
                    os.remove('pmid {%s - %s}.csv' % (starting_pmid, intermediate_pmid))
                    print ("File " + str(starting_pmid) + " - " + str(intermediate_pmid) + " has been removed.")
                else:
                    print ("File " + str(starting_pmid) + " - " + str(intermediate_pmid) + " is not empty.")

                starting_pmid = intermediate_pmid + 1
                intermediate_pmid = intermediate_pmid + 100000
        else:
            print("Entering base case ...")
            with open('pmid {%s - %s}.csv' % (starting_pmid, ending_pmid), mode='r') as csv_file:
                reader = csv.reader(csv_file)

                if len(list(reader))==1:
                    os.remove('pmid {%s - %s}.csv' % (starting_pmid, ending_pmid))
                    print ("File " + str(starting_pmid) + " - " + str(ending_pmid) + " has been removed.")
                else:
                    print ("File " + str(starting_pmid) + " - " + str(ending_pmid) + " is not empty.")
            break
                
                


        #94357012, total rows
        #51556076, null affiliation
        #42800936, not null affiliation
        #21, minimum pmid
        #32078260, maximum pmid
        # print(len(temp_row))

    sys.exit('Script completed')

except (Exception, psycopg2.Error) as error:
    sys.exit('Script failed')
