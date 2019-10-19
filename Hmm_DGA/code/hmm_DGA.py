import numpy as np
import matplotlib.pyplot as plt
import csv
import joblib # a library to run python code in parallel
from hmmlearn import hmm
  

# filter the length of the domains to be no less than......
MIN_LEN = 10

# number of states of Makov process
N = 10

# where the model arguments stored
MODEL_PATH = "../model/hmm_dga.m"

# path of Alexa domain file and DGA domain file
ALEXA_PATH = "../../data/top-1000.csv"
CRYPTOLOCKE_PATH = "../../data/dga-cryptolocke-1000.txt"
POSTTOVARGOZ_PATH = "../../data/dga-post-tovar-goz-1000.txt"

def trainHmm():
	domains = loadAlexaDomains(ALEXA_PATH)
	X = [[0]]
	# the lenth of each domain
	XLens = [1]

	# convert each character of each domain to ASCII value, put them in X
	for domain in domains:
		vec = domainToVec(domain)
		# convert vector to numpy array
		npArray = np.array(vec)
		# append the new numpy array vector to the end of X
		X = np.concatenate([X, npArray])
		XLens.append(len(npArray))

	#print("******start training*******")
	
	model = hmm.GaussianHMM(n_components=N, covariance_type="full", n_iter=100)
	model.fit(X, XLens)

	#print("******end training*******")
	# save the trained model for future testing, no usage here
	joblib.dump(model, MODEL_PATH)

	return model

def testHmm(model, domains):
	#model = joblib.load(MODEL_PATH)
	X = []
	y = []

	for domain in domains:
		vec = domainToVec(domain)
		npArray = np.array(vec)
		label = model.score(npArray)

		# here we appnend domain length instead of domain itself
		# this shall show interesting things in the plot
		X.append(len(domain))  
		y.append(label)

	return X,y

def plotResult(X1, y1, X2, y2, X3, y3):
	fig, ax = plt.subplots()
	ax.set_xlabel("Domain Length")
	ax.set_ylabel("HMM test result")

	ax.scatter(X1, y1, color = "r", label = "Alexa")
	ax.scatter(X2, y2, color = "b", label = "Cryptolocke")
	ax.scatter(X3, y3, color = "g", label = "Post-tovar-goz")

	ax.legend(loc = "lower left")

	plt.show()

# convert each domain an ASCII array
def domainToVec(domain):
	result = []
	for i in range(len(domain)):
		result.append([ord(domain[i])])

	return result

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
	model  = trainHmm()
	X1, y1 = testHmm(model, loadAlexaDomains(ALEXA_PATH))
	X2, y2 = testHmm(model, loadDGADomains(CRYPTOLOCKE_PATH))
	X3, y3 = testHmm(model, loadDGADomains(POSTTOVARGOZ_PATH) )

	plotResult(X1, y1, X2, y2, X3, y3)