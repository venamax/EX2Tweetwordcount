import psycopg2
import sys



 
# Get the total number of args passed to the finalresults.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)

 

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if total > 1:

    low_range = sys.argv[1]*1
    high_range = sys.argv[2]*1
    cur.execute("SELECT word, count FROM Tweetwordcount WHERE count > %s AND count < %s",(low_range,high_range))
    records = cur.fetchall()
    for rec in records:
        print """  "%s": %s"""%(reco[0],rec[1])
    conn.commit()
else:
    print "No range given"



 