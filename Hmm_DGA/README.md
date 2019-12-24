## Dectect DGA domains with Hidden Markov Model

## Dataset: 
  Regular domains: Alexa top domains
  
  DGA domains: cryptolocke and post-tovar-goz

### 1.	Create the Hidden Makov Model
#### DGA(Domain Generation Algorithm) usually is an algorithm based on current time, hardcoded constants and dictionary.
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/Hmm_DGA/pics/DGA.png)
#### Take the DGA of Cryptolocker as an example, the relationship between DGA generated domains and time is as follows:
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/Hmm_DGA/pics/DGA_domain_vs_time.png)
### 2.	Feature Extraction:
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/Hmm_DGA/pics/DGA_feature_extraction.png)
#### Alexa is a professional website publishing world domain rankings. It was originally founded with search engine as its major service in April, 1996(USA). Alexa collects more than 1000GB data from  internet every day. Alexa provides billions of URLs, as well as the rankings of most visited domains. As we know, Alexa is the website which provides the largest quantity of URLs and domain rankings. We utilize the domains of Alexa top 1 million websites to train the HMM model.
![image](https://github.com/jling0906/Cyber-Security-with-Machine-Learning/blob/master/Hmm_DGA/pics/Alexa_domain_rankings.png)
#### To test the model, we use the Botnet domains from Cryptolocker and post-tovar-goz.
## References:
https://github.com/duoergun0729/1book
