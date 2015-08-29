from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import num2words

D=[]
porter_stemmer = PorterStemmer()

#To tokenize and to convert inot lower case,removal of stop words.
def word_tokenize_all(list):
	
	punctuations=['+',',','?','!','/','@','#','$']
	tokens=[]
	
	for lines in list:
		all_words=word_tokenize(lines)	
		all_words=map(lambda x:x.lower(),all_words)
		filtered_words = [word for word in all_words if word not in stopwords.words('english')+punctuations]
		stemmed_word=[porter_stemmer.stem(word) for word in filtered_words]
		add_numbers=[num2words.num2words(int(words)) if words.isnumeric() else words  for words in stemmed_word]
		
		tokens.append(add_numbers)
		
	return tokens



fp=open('dataset.txt','r')

list=[line.replace(',', ' ') for line in fp.readlines()]

D=word_tokenize_all(list)
fp.close()

