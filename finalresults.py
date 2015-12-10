import psycopg2
import cmd, sys

def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')
        else: 
            input_word = self.lastcmd
            print input_word
            cur.execute("SELECT count FROM Tweetwordcount WHERE word=Chavez")
            input_count = cur.fetchall()
            print "Total number of occurences of ""Chavez"": %s"%(input_count)

emptyline(cmd.Cmd)

