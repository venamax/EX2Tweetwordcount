import psycopg2

input_word = raw_input('--> ')
input_word = str(input_word)

input_word = input_word[0:len(input_word)]

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if input_word != '':

    cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s", (input_word))
    input_count = cur.fetchall()
    print "Total number of occurences of ""%s"": %s"%(input_word, input_count)

else:
    print "O h yeah"