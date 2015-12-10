import psycopg2
import sys

 
# Get the total number of args passed to the finalresults.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)

def wrapper(s1):
    return "'%s'" % s1
 
# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if total > 1:

    input_word = wrapper(sys.argv[1])
    print input_word
    cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s", (input_word,))
    input_count = cur.fetchall()
    print " Total number of occurences of %s: %s"%(input_word,input_count[0])
else:
    print "yeahhnnnh"


 