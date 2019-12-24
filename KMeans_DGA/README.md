Domain Generation Algorithm(DGA) is a mature and active technology, on which is centralized Botnet relies. Researchers have to quickly find the generation algorithm in order to shut down the Botnet. This project is to user K-Means clustering to detect the DGA domains.
## Libraries:
sklearn
### Data:
Legit domains come from [Alexa](https://www.alexa.com/topsites).

DGA domains come from cryptolocker and post-tovar-goz.
## 1.	Data Collection and Data Cleaning
Load top 100 domains from Alexa as positive data. Label them as 0. Also load the DGA domains from cryptolocker and post-tovar-goz, which are to be labeled as 2 and 3.
## 2.	Feature extraction:
Convert the domains to 2-gram sequences
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/KMeans_DGA/pics/KMeans_DGA.png)
## 3.	Training : 
K-Means algorithm
## 4.	Testing:
Do dimensionality reduction with t-distributed Stochastic Neighbor Embedding(TNSE) to plot the clustering in 2-d graph.

Notes: From my testing, this model is actually not very good with just top 100 Alexa domains. My guess is the size of data is too small(100). Will try with more data in the future tests.

### References:
https://github.com/duoergun0729/1book
