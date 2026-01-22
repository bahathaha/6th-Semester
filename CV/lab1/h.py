import random
  1 
  2 
  3 class BayesianCoinToss:
  4   def __init__(self,initial_probability_heads):
  5     self.probability_heads=initial_probability_heads
  6 
  7 
  8   def biased_coin_toss(self):
  9 
 10     #Generate a random number between 0 and 1
 11 
 12     random_number = random.random()
 13 
 14     #Determine the outcome based on the current probability
 15 
 16     if random_number<self.probability_heads:
 17 
 18        outcome = 'Heads'
 19 
 20    else:
 21 
 22       outcome = 'Tails'
 23 
 24 
 25       return outcome
 26  
 27  
 28   def update_probability(self,outcome):
 29  
 30     #update probability based on observed outcome 
 31  
 32     if outcome == 'Heads':
 33   
 34        self.probability_heads+=0.1
 35     else:
 36   
 37        self.probability_head-=0.1
 38    
 39    
 40      #ensure probability remains within [0,1] 
 41    
 42       self.probability_heads = max(0.0, min(1.0,self.probability_heads))
 43    
 44    
 45  def main(): 
 46    
 47    #initial probability of getting heads 
 48    
 49    initial_probability_heads=0.5
 50    
 51   #number of coin tosses 
 num_tosses=10
 24 
 23 
 22    #create bayesian coin toss model 
 21 
 20    coin_toss_model
 19 
 18  BayesianCoinToss(initial_probability_heads)
 17 
 16    #perform coin tosses and update probabilities 
 15 
 14    for _ in range(num_tosses):
 13 
 12         result = coin_toss_model.biased_coin_toss()
 11 
 10         print(f"Biased coin toss result: {result}")
  9 
  8 
  7         coin_toss_model.update_probability(result)
  6 
  5        print(f"Updated probability of getting heads:{coin_toss_model.probability_heads:.2f}")
  4 
  3 
  2        if __name__ == "__main__":
  1 
79            main()
