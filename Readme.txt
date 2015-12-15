Instructions to run application

1.	Connect to instance
2.	Start counter from scratch. CLI: $python dropaddtable.py
3.	Turn on the data hose by typing “sparse run” on the EX@Tweetwordcount directory where all files reside. CLI: $sparse run
4.	To find out the count associated to a specific term run the following line on the CLI: $python finalresults.py ,<search_term>
5.	To list all terms and their counts at any moment run the following line on the CLI: $python finalresults.py
6.	Use Tableau to connect to the Postgres database to generate visualizations making sure that port 5432.

Key Files  and Data Directory

EX2Tweetwordcount/
Twittercredentials.py: file that contains authentication information required to connect to Twitter’s API.

Finalresults.py: script that returns words and their corresponding counts. Adding a term after running the script on the CLI will also give you the specific amount of occurrences of that specific term.

EX2Tweetwordcount/src/spouts
tweets.py: file that collects tweets through Twitter’s API.

EX2Tweetwordcount/src/bolts
parse.py: file that breaks each tweets into valid words.

wordcount.py: file that stores words and its corresponding counts in a Postgres database.

EX2Tweetwordcount/src/topologies
tweetwordcount.clj: file that describes how spouts and bolts work together.

Postgres:
Database: tcount
Table: Tweetwordcount

AMI:
ucbw205_complete_plus_ postgres_PY2.7.
