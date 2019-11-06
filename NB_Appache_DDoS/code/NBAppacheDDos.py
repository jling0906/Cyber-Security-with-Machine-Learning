import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB


# load data from KDD99 dataset
def loadKDD99(path):
	data=[]
	with open(path) as file:
		for line in file:
			line = line.strip("\n")
			line = line.split(",")
			data.append(line)
	return data

# filter data which be labled with http, also labeled with apache or normal
def getAppacheNormalHttpData(data):
	filtedData = []
	X = []
	y = []

	for row in data:
		if ( row[41] in ["apache2.", "normal."] ) and ( row[2] == "http" ):
			if row[41] == "apache2.":
				y.append(1)
			else: 
				y.append(0)

			newRow = [row[0]] + row[4:8] + row[22:30] + row[31:40]
			filtedData.append( newRow )

	print(len(data))

	for row in filtedData:
		rowX = []
		for val in row:
			rowX.append(float(val))

		X.append(rowX)

	return X, y


if __name__ == "__main__":
	data = loadKDD99("../data/corrected.txt")
	X,y = getAppacheNormalHttpData(data)
	clf = GaussianNB()
	print(len(X))
	print(len(y))
	print(cross_val_score(clf, X, y, n_jobs=-1, cv=10))












