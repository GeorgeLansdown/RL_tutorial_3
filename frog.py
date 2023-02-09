class agent(object):
    def __init__(self):
        self.policy = {'rock_0':{'rock_1':1}, 'rock_1':{'rock_0':1/2, 'land':1/2}, 'land':{'land':1}}
        self.V = {'rock_0':0, 'rock_1':0, 'land':0}
        self.epsilon = 0.01
        
        
        for i in range(2):
            self.policy_iterate(1)
            self.change_policy()
        
    def reward(self, state1, state2):
        if state1 == 'rock_1' and state2 == 'land':
            return 10
        return 0
    
    def transition_prob(self,state1, state2):
        if state1 == state2:
            return .1
        return .9
    
    def options(self, state):
        return list(self.policy[state].keys())
                    
    
    def policy_iterate(self, i):
        delta = 0
        
        print("policy iteration: %s" % i)
        
        old_policy = self.V
        
        for state, value in old_policy.items():
            
            s=0
            
            for state_prime in self.options(state):
                prob = self.policy[state][state_prime]

                
                transition_prob = self.transition_prob(state, state_prime)
                reward_jump = self.reward(state, state_prime)
                reward_not_jump = self.reward(state,state)
                
                s+= prob*(transition_prob*(reward_jump+0.9*old_policy[state_prime]) + ((1-transition_prob)*(reward_not_jump+.9*old_policy[state])))
            
            delta = max(delta, abs(value-s))
            
            
            self.V[state] = s
        
        
        if delta >= self.epsilon:
            print("state value: %s" % self.V)
            self.policy_iterate(i+1)
        else:
            print("terminating because delta = %s" % delta)
    
    
    def change_policy(self):

        print("\n starting policy: %s \n" % self.policy)
        
        for state in list(self.policy.keys()):
        
            options=[]
            for state_prime in self.options(state):
                s=self.policy[state][state_prime]*(self.reward(state,state_prime) + .9*self.V[state_prime])
                options.append((state_prime, s))

            best = max(options, key=lambda x: x[1])[0]
            
            for option in self.policy[state]:
                if option == best:
                    self.policy[state][option] = 1
                else:
                    self.policy[state][option] = 0
                    
        print("\n new policy: %s" % self.policy)
        
        
a = agent()
