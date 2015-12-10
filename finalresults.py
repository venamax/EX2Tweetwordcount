import psycopg2

input_word = raw_input(str(input))

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if input_word != '':

    cur.execute("SELECT count from Tweetwordcount WHERE word = %s", % (input_word))
    input_count = cur.fetchall()
    print "Total number of occurences of ""%s"": %s"%(input_word, input_count)

else:
    print "O h yeah"