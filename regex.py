import re
import sqlite3

#conn = sqlite3.connect('flight-details')
#conn.execute('''CREATE TABLE FLIGHT_DATA 
#		(FLIGHT_NUM	INT	NOT NULL,
#		AIRLINE	TEXT NOT NULL,
#		FINAL_DEST TEXT NOT NULL,
#		TAKEOFF_AIRPORT TEXT NOT NULL,
#		ORIG_TAKEOFF_DATE INT NOT NULL,
#		TAKEOFF_TIME INT NOT NULL,
#		FLIGHT_STATUS TEXT NOT NULL);''')

f = open('flights.txt')
outputfile = open('output.txt', 'w')

strToSearch=''

for line in f:
    strToSearch += line

findPat1 = re.findall(r'(ffFidsArrivals.+)title="Flight Details">(.*?)</a></div>', strToSearch)
findPat2 = re.findall(r'/(\)\n)/g', strToSearch)

#patFinder2= re.compile('(ffFidsArrivals.+)', re.IGNORECASE)
#findPat2 = re.findall(patFinder2, strToSearch)

for i in findPat1:
    print(i)
    outputfile.write(str(i)+'\n')

#conn.execute("INSERT INTO FLIGHT_DATA (FLIGHT_NUM,AIRLINE,FINAL_DEST,TAKEOFF_AIRPORT,ORIG_TAKEOFF_DATE,TAKEOFF_TIME,FLIGHT_STATUS) VALUES($1,$2,$3,$4,$5,$6,$7)", [strToSearch]);	
outputfile.close()
f.close()
#conn.close()
