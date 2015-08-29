#TF-IDF
**TASK**<br>
Given a query string q and a corpus of documents, retrieve the top k documents that are the closest match to query string using tf-idf

**Dataset**<br>
Has a list of cricket commentary units in the file dataset.txt. A single unit of cricket commentary is the commentary for 1 ball and this constitutes 1 document.</br></br>


**Packages that are to be installed before executing the program**</br>
1.nltk(natural language toolkit)</br>
2.num2words(installation command: sudo pip install num2words)</br></br>

**Commands for executing the program**</br>
python tfidf.py</br></br>

**Sample Input and Output**</br>

enter the query string: or q to quit</br>
driven through midwicket for a couple of runs</br>
**************************************************************</br>
rank: 1 score 1.05838456103</br>
Anderson to Rogers 2 runs too straight and tucked off the pads through midwicket  an easy couple</br>
-----------------------------------------------</br>
rank: 2 score 1.01438166749</br>
Jarvis to Jahurul Islam 2 runs ooh  swing there  turns out to be too full and that's driven through midwicketfor a couple of runs</br>
-----------------------------------------------</br>
rank: 3 score 0.962167782759</br>
Broad to Williamson 2 runs little too straight and tucked past midwicket so they get a couple</br>
-----------------------------------------------</br>
rank: 4 score 0.723499546899</br>
Southee to Cook no run driven to cover</br>
-----------------------------------------------</br>
rank: 5 score 0.723499546899</br>
Southee to Trott no run driven into the covers</br>
-----------------------------------------------</br></br>


enter the query string: or q to quit</br>
"around the wicket"(exact search similar to google search)</br>
**************************************************************</br>
rank: 1 score 1.02036361107</br>
Broad to Rogers no run around the wicket  Rogers back and across the off stump to block up the wicket</br>
-----------------------------------------------</br>
rank: 2 score 0.526893945533</br>
Swann to Rogers 1 run around the wicket to the leftie but too straight and played calmly off the back foot into midwicket for a single</br>
-----------------------------------------------</br>
rank: 3 score 0.491767682498</br>
Anderson to Rogers 1 run around the wicket  slants back in  Rodgers uses the angle and clips out to deep square leg</br>
-----------------------------------------------</br>
rank: 4 score 0.461032202341</br>
Swann to Rogers no run Rogers plays back to Swann around the wicket  flicks it to square leg but can't find a run</br>
-----------------------------------------------</br>
rank: 5 score 0.433912661027</br>
Anderson to Rogers FOUR around the wicket but too straight just back of a length  clipped through square leg and it's well timed  runs away from the fielder</br>
-----------------------------------------------</br>
enter the query string: or q to quit</br>
q
