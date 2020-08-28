import psycopg2
import sys
from nltk.tokenize import sent_tokenize 
import re
import csv



# 32025678 having no dot at end
# 32025676 having dot at end


try:
    starting_pmid = 21
    intermediate_pmid = 100000
    ending_pmid = 32078260

    while 1:
        if intermediate_pmid<ending_pmid:
            #open existing csv files
            with open('pmid [%s - %s].csv' % (starting_pmid, intermediate_pmid), mode='r') as csv_file:
                reader = csv.reader(csv_file)
                print("Reading file: " + str(starting_pmid) + " - " + str(intermediate_pmid))
                #making new csv files
                with open('pmid {%s - %s}.csv' % (starting_pmid, intermediate_pmid), mode='w') as new_csv_file:
                    #creating header for csv files
                    print("Writing file: " + str(starting_pmid) + " - " + str(intermediate_pmid))
                    fieldnames = ['pmid', 'forename', 'lastname', 'email', 'date_year', 'urls']
                    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
                    writer.writeheader()

                    for row in reader:
                        #ignoring header of original file
                        if row[0]=='pmid':
                            pass
                        elif row[3].endswith('.'):
                            #write operation and checking if there is a dot at last index of email
                            writer.writerow({'pmid': row[0], 'forename': row[1], 'lastname': row[2], 'email':row[3][:-1], 'date_year': row[4],'urls': row[5]})
                        else:
                            writer.writerow({'pmid': row[0], 'forename': row[1], 'lastname': row[2], 'email': row[3], 'date_year': row[4],'urls': row[5]})
                    print("Done writing file: " + str(starting_pmid) + " - " + str(intermediate_pmid))

                starting_pmid = intermediate_pmid + 1
                intermediate_pmid = intermediate_pmid + 100000
        else:
            print("Entering base case ...")
            with open('pmid [%s - %s].csv' % (starting_pmid, ending_pmid), mode='r') as csv_file:
                #opening last file
                reader = csv.reader(csv_file)
                print("Reading file: " + str(starting_pmid) + " - " + str(ending_pmid))
                #making new csv files
                with open('pmid {%s - %s}.csv' % (starting_pmid, ending_pmid), mode='w') as new_csv_file:
                    print("Writing file: " + str(starting_pmid) + " - " + str(ending_pmid))
                    fieldnames = ['pmid', 'forename', 'lastname', 'email', 'date_year', 'urls']
                    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
                    writer.writeheader()

                    for row in reader:
                        #ignoring header of original file
                        if row[0]=='pmid':
                            pass
                        elif row[3].endswith('.'):
                            #write operation and checking if there is a dot at last index of email
                            writer.writerow({'pmid': row[0], 'forename': row[1], 'lastname': row[2], 'email': row[3][:-1], 'date_year': row[4],'urls': row[5]})
                        else:
                            writer.writerow({'pmid': row[0], 'forename': row[1], 'lastname': row[2], 'email': row[3], 'date_year': row[4],'urls': row[5]})
                    print("Done writing file: " + str(starting_pmid) + " - " + str(ending_pmid))
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
