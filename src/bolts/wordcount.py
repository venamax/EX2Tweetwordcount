from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
#Create a Table
#The first step is to create a cursor. 

        cur = conn.cursor()
        cur.execute('''CREATE TABLE Tweetwordcount
        (word TEXT PRIMARY KEY     NOT NULL, count INT     NOT NULL);''')
        conn.commit()
##        conn.close()   
     

    def process(self, tup):
        word = tup.values[0]
        cur = conn.cursor()  
        #Insert
        cur.execute("INSERT INTO Tweetwordcount (word,count) \
              VALUES (word, 1)");
        conn.commit()
        
        
        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (word, self.counts[word]))
        conn.commit()

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
