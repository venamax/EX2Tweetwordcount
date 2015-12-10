import psycopg2
import sys
import urllib2
 
# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)

 
# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if total > 1:
    input_word = str(sys.argv[1])
    input_word = dict(input_word=input_word)
    print input_word.values
    cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s",input_word.values)
    input_count = cur.fetchall()
    print """ Total number of occurences of "%s": %s"""%(input_word,input_count[0][0])
else:
    print "yeahhh"


 