from abc import ABC,abstractmethod

# State machines
# Any software /code/ process/ Function(s), which doesn't terminates immediately after doing work is a State Machine

# We want to easily identiry states and events in state machines
# It must be easy for a programmer to expand States and Events
# focus more on what to do



# create a template of states and events

class State(ABC):
    
    #abstractmethods must be implemented in the derived class
    @abstractmethod
    def in_state(self):
        pass
    
class HappyState(State):
    
    def in_state(self):
        print("I am in Happy state")

class SadState(State):
    
    def in_state(self):
        print("I am in Sad state")
        
        
# unable to execute since cant instantiate abstract class State with abstract method in_state
# s1 = State()