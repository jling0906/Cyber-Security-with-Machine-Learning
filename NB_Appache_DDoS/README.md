### This project is to detect Apache DDoS attack.
DDoS (Distributed Denial-of-Service) attack is to disrupt normal traffic of a targeted server, service or network for hours even for days by overwhelming the target or its surrounding infrastructure with a flood of internet traffic.
### Libraries: 
  sklearn
### Dataset: 
  KDD99
## 1.	Data collection and data cleaning:
The dataset is called KDD99. Here is an review of it(https://peerj.com/preprints/1954/). KDD99 dataset was actually been cleaned already. In KDD99, each connection comes with 41 features.
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/NB_Appache_DDoS/pics/NB_DDoS_KDD99.png)
Only some of the 41 features are related with DDoS.
### 1)	The basic features the network connection.
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/NB_Appache_DDoS/pics/NB_DDoS_table1.png)
### 2)	The network traffic related features based on time
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/NB_Appache_DDoS/pics/NB_DDoS_table2.png)
### 3)	The network traffic related features based on target machine
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/NB_Appache_DDoS/pics/NB_DDoS_table3.png)
Load the data from KDD99 dataset, filter the data with the label of “appache2” or “normal”, also have to be labeled with “http”. 
## 2.	Feature extraction:
Select the features related with DDoS.
## 3.	Training: 
Naïve Bayes algorithm
## 4.	Testing:
Ten-fold cross validation. 
The accurate rate is 99%.
### References:
https://github.com/duoergun0729/1book.
https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/
