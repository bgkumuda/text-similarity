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

## Git command to clone the repo
 git clone https://github.com/bgkumuda/text-similarity.git	
			
## Steps to execute in terminal 1
1. docker pull kumudabg/text-simililarity-service:1.0
2. docker build -t kumudabg/text-simililarity-service:1.0 . (not required if no change made to the code after pulling the image from docker hub)
3. docker run -p 5000:5000 kumudabg/text-simililarity-service:1.0

## Steps to execute in terminal 2
#### Compare the text 1 and 2
curl -X POST -H "Content-Type: application/json" -d '{"text1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you.", "text2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}' http://127.0.0.1:5000/compare_texts

#### Compare the text 1 and 3
curl -X POST -H "Content-Type: application/json" -d '{"text1": "The easiest way to earn points with Fetch Rewards is to just shop forthe products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you.", "text2": "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'\''ll give you the points whether or not you knew about the offer. We just think it is easier that way."}' http://127.0.0.1:5000/compare_texts

#### Compare two unique texts
curl -X POST -H "Content-Type: application/json" -d '{"text1": "He came", "text2": "I am going"}' http://127.0.0.1:5000/compare_texts

#### Compare two identical texts
curl -X POST -H "Content-Type: application/json" -d '{"text1": "I am going", "text2": "I am going"}' http://127.0.0.1:5000/compare_texts



