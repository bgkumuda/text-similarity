# Documentation	
					
## Fetch Rewards : Machine Learning Engineer role
## Name: Kumuda Benakanahalli Guruprasada Murthy
		
### 1. Do you count punctuation or only words?
Jaccard Similarity is used to calculate the text similarity. Punctuations are not considered or the calculation

### 2. Which words should matter in the similarity comparison?
All the words are considered in thai approach

### 3. Do you care about the ordering of words?
No, the set of tokens from text matters

### 4. What metric do you use to assign a numerical value to the similarity?
The resulting Jaccard similarity coefficient will always be in the range [0, 1], where 0 indicates no similarity (no common elements between sets) and 1 indicates complete similarity (identical sets).
For the texts, Jaccard similarity can be defined as the size of the intersection of two sets to the size of the union of two sets. 
I.e. J(A,B) = |(A ∩ B)| / |(A U B)|

### 5. What type of data structures should be used? (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)
Set is the data structure used to store the tokens .
			
## End to end process:
1. The two input texts are received from the request.
2. Jaccard similarity is calculated after removing the punctuations.
3. The similarity score is forwarded if there is no error during the flow. Else error message with error code: 500 is sent 	
				
## To retrieve the base image from dockerhub : 
docker pull kumudabg/text-simililarity-service:1.0				
Reference: https://hub.docker.com/r/kumudabg/text-simililarity-service/tags
					
## Options to improve the performance,scalability and reliability
1. Containerization to attain uniformity across environments - achieved through docker
2.Production ready web server to handle several requests at once using gunicorn
3. Secure communication over https
4. Alter the number of instances dynamically upon reacting to incoming traffic - can be achieved through kubernetes /cloud service
5. Load balancing to distribute the incoming requests to multiple instances - can be achieved through cloud service
					
## Steps to execute
1. docker pull kumudabg/text-simililarity-service:1.0
2. docker build -t text-simililarity-service:1.0 . (not required if no change made to the code after pulling the image from docker hub)
3. docker run -p 5000:5000  text-simililarity-service:1.0

