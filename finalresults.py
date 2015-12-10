
import psycopg2
from cmd import Cmd

class MyPrompt(Cmd):
    
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    
    def have_word(self, args):
        """find the count for a given word"""
        if len(args) == 0:
            print "No argument"
        else:
            input_word = args
            
        print input_word
        cur.execute("SELECT count FROM Tweetwordcount WHERE word='%s'", (input_word))
        input_count = cur.fetchall()
        print "Total number of occurences of ""%s"": %s"%(input_word,input_count[0])


    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
