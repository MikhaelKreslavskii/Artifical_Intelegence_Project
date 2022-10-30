# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
   # print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    "*** YOUR CODE HERE ***"
    
    
    Stack=util.Stack()
    #Stack=[]
    #path=[]
    #visited.append(problem.getStartState())
    
          
            
    
    current_state=problem.getStartState()
    # initialize the start state
    visited=[] #list of visited nodes
    current_state_and_action=(current_state,[]) #tuple of pacman current state and chosen action
    Stack.push(current_state_and_action) #pushing to Stack
    
    while(not Stack.isEmpty()): # while something in the Stack
        
       current_state,path=Stack.pop() # pop our current_state and chosen move
       #print(visited)
       print(path)
       if problem.isGoalState(current_state):  # if it is a goal state we return whole path
                        print(current_state)
                        
                        visited.append(current_state)
                        
                        return path
       
       visited.append(current_state) # mark our node as visited
            
       for action in problem.getSuccessors(current_state):  # go through possible actions
                
            if action[0] not in visited:
                print("not visited node is ", action[0])
                print("I should do ", action[1])
                
                path_t=action[1]
                Stack.push((action[0],path+[path_t]))
                
        
               
        
        
    
   
            
    
    
    
    
  
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #it is like dfs but changing the stack for a Queue and marking nodes as visited inside for loop
    Queue=util.Queue()
    #Stack=[]
    #path=[]
    #visited.append(problem.getStartState())
    
          
            
    
    current_state=problem.getStartState()
    # initialize the start state
    visited=[] #list of visited nodes
    visited.append(current_state)
    current_state_and_action=(current_state,[]) #tuple of pacman current state and chosen action
    Queue.push(current_state_and_action) 
    
    while(not Queue.isEmpty()): 
        
       current_state,path=Queue.pop() # pop our current_state and chosen move
       #print(visited)
       #print(path)
       if problem.isGoalState(current_state):  # if it is a goal state we return whole path
                        #print(current_state)
                        
                        
                        
                        return path
       
        # mark our node as visited
            
       for action in problem.getSuccessors(current_state):  # go through possible actions
                
            if action[0] not in visited:
                
                visited.append(action[0]) # mark as visited all possible node
                path_t=action[1]
                Queue.push((action[0],path+[path_t]))
                
        
               
    
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    Queue=util.PriorityQueue()
    current_state=problem.getStartState()
    visited=[]
    
    Queue.push((current_state,[]),0)
    while(not Queue.isEmpty()):
        current_state,path=Queue.pop()
        if problem.isGoalState(current_state):
            return path
        if current_state not in visited:
            visited.append(current_state)
            for action in problem.getSuccessors(current_state):
                if action[0] not in visited:
                    #visited.append(current_state)
                    path_t=action[1]
                    Queue.push((action[0],path+[path_t]),problem.getCostOfActions(path+[path_t]))
        
    
    util.raiseNotDefined()
   
    
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    Queue=util.PriorityQueue()
    current_state=problem.getStartState()
    visited=[]
    
    Queue.push((current_state,[]),0)
    while(not Queue.isEmpty()):
        current_state,path=Queue.pop()
        if problem.isGoalState(current_state):
            return path
        if current_state not in visited:
            visited.append(current_state)
            for action in problem.getSuccessors(current_state):
                if action[0] not in visited:
                    #visited.append(current_state)
                    path_t=action[1]
                    Queue.push((action[0],path+[path_t]),problem.getCostOfActions(path+[path_t])+heuristic(action[0],problem))
        
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
