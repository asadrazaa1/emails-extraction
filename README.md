# emails-extraction


# Fetch-emails.py
Purpose of the this file is to establish a connection on a remote postgreSql database and extracting required data from two schemas. Used a regex expression to extract emails from text, finally in the end generated csv files with generic naming convention. The original data was 90 millon plus, this script also created some csv files which were empty, as database had no emails against some users.

# Remove-email-dots.py
For all the emails in csv files, some emails had dots at the end. To filter clean emails, I indexed each csv file and created new csv files.

# Remove-empty-csv's.py
While creating csv files, I received 100+ csv files which were empty, instead of removing these files manually, I used this script to remove empty csv files.
