import psycopg2
import sys
from nltk.tokenize import sent_tokenize 
import re
import csv


try:
    #connecting with database
    connection = psycopg2.connect(user="database-user",
                                  password="database-password",
                                  host="host-ip-address",
                                  port="5432",
                                  database="data-base-name")

    #using divide rule method to access data between some range
    starting_pmid = 21
    intermediate_pmid = 100000
    maximum_pmid = 32078260
    base_url = 'https://pubmed.ncbi.nlm.nih.gov/'

    
    
    while (1):
        if(intermediate_pmid<maximum_pmid):
            with connection.cursor() as cursor:
		#query to extract specific data from database
                temp_query = """select a.pmid, a.forename, a.lastname, a.affiliation, b.date_year from pm2o.author a
	                            inner join pm2o.studies b on a.pmid = b.pmid 
                                where a.affiliation is not null and 
                                a.pmid between '{}' and '{}';""".format(starting_pmid, intermediate_pmid )
                cursor.execute(temp_query)
                temp_data = cursor.fetchall()
                print("Fetched data from db ...")

            print(str(starting_pmid) + "  -  " + str(intermediate_pmid))

            
            #making csv files
            with open('pmid [%s - %s].csv' % (starting_pmid, intermediate_pmid), mode='w') as csv_file:
		#creating header for csv file
                fieldnames = ['pmid', 'forename', 'lastname', 'email', 'date_year', 'urls']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for data in temp_data:
		    #using regex on data[3] column i.e original data
                    match = re.findall(r'[\w\.-]+@[\w\.-]+', str(data[3]))
                    if len(match) != 0:
			#csv write operation
                        writer.writerow({'pmid': data[0], 'forename': data[1], 'lastname': data[2], 'email':match[0], 'date_year': data[4],'urls': base_url + str(data[0])})
            

            print("For loop ended ...")
            print("Data written into file ...")

            starting_pmid = intermediate_pmid + 1
            intermediate_pmid = 100000 + intermediate_pmid

        else:
            print("Entering base case")

            with connection.cursor() as cursor:
		#query to extract specific data from database
                temp_query = """select a.pmid, a.forename, a.lastname, a.affiliation, b.date_year from pm2o.author a
	                            inner join pm2o.studies b on a.pmid = b.pmid 
                                where a.affiliation is not null and 
                                a.pmid between '{}' and '{}';""".format(starting_pmid, maximum_pmid )
                cursor.execute(temp_query)
                temp_data = cursor.fetchall()
                print("Fetched data from db ...")

            print(str(starting_pmid) + "  -  " + str(maximum_pmid))

            
            #making csv file
            with open('pmid [%s - %s].csv' % (starting_pmid, maximum_pmid), mode='w') as csv_file:
		#creating header for csv file
                fieldnames = ['pmid', 'forename', 'lastname', 'email', 'date_year', 'urls']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for data in temp_data:
		    #using regex on data[3] column i.e original data
                    match = re.findall(r'[\w\.-]+@[\w\.-]+', str(data[3]))
                    if len(match) != 0:
			#csv write operation
                        writer.writerow({'pmid': data[0], 'forename': data[1], 'lastname': data[2], 'email':match[0], 'date_year': data[4],'urls': base_url + str(data[0])})
            

            print("For loop ended ...")
            print("Data written into file ...")
            break



        #94357012, total rows
        #51556076, null affiliation
        #42800936, not null affiliation
        #21, minimum pmid
        #32078260, maximum pmid
        # print(len(temp_data))

    sys.exit('Script completed')

except (Exception, psycopg2.Error) as error:
    print("connection error: ", error)
    sys.exit('Script failed')
sys.exit(0)




