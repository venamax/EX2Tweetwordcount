from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

     

    def process(self, tup):
        word = tup.values[0]
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()  
        initial_count = 1
        
        cur.execute("SELECT word, count from Tweetwordcount")
        records = cur.fetchall()
        repeat_word = False
        for rec in records:
            if rec[0] == word:
                repeat_word= True    
        
        if repeat_word == True:
        # Increment the local count
            self.counts[word] += 1
            self.emit([word, self.counts[word]])

            cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word],word))
            conn.commit()
        
        else:
        #Insert
            cur.execute("INSERT INTO Tweetwordcount (word,count) \
                  VALUES (%s, %s)", (word,initial_count)) ;
            conn.commit()
        


        

        
        

        
        conn.close()   
        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        



        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
