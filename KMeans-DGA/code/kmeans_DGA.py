import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

# a random seed for random generator, no specific meaning
RANDOM_STATE = 100

# filter the length of the domains
MIN_LEN = 10

def kmeans_dga():
	# get top 100 normal domains from Alexa rankings
	x1 = loadAlexaDomains("./data/top-1000.csv")
	# get DGA domains
	x2 = loadDGADomains("./data/dga-cryptolocke-1000.txt")
	x3 = loadDGADomains("./data/dga-post-tovar-goz-1000.txt")

	# "mix" the legit and malicious domains into one list
	xDomains = np.concatenate((x1, x2, x3), axis=0)

	cv = CountVectorizer(ngram_range = (3, 3),
						 decode_error = "ignore",
						 token_pattern =r"\w",
						 min_df = 1 )

	# convert the domain list to 2-grams of words as feature vectors
	x = cv.fit_transform(xDomains).toarray()
	model = KMeans(n_clusters = 2, random_state = RANDOM_STATE)

	y_pred = model.fit_predict(x)

	# Dimensionality reduction for data visualization
	tsne = TSNE(learning_rate = 100)
	x = tsne.fit_transform(x)

	#show the result in 2-d form
	for i, label in enumerate(x):
		x1, x2 = x[i]
		if y_pred[i] == 1:
			plt.scatter(x1, x2, marker = 'o')
		else:
			plt.scatter(x1, x2, marker = 'x')

	plt.show()

# load top 100 normal domains from Alexa rankings csv file
def loadAlexaDomains(path):
	result = []
	file = csv.reader(open(path))
	for line in file:
		domain = line[1]
		if len(domain) >= MIN_LEN:
			result.append(domain)
	return result

# get DGA domains from text files
def loadDGADomains(path):
	result = []
	with open(path) as file:
		for line in file:
			domain = line.split(",")[0]
			if len(domain) >= MIN_LEN:
				result.append(domain)
				if len(result) == 500:
					break
	return result

if __name__ == '__main__':
	kmeans_dga()