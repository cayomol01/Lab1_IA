class FrameWork():
    def __init__(self, initial, goal, img_arr):
        self.initial = initial
        self.goal = goal
        self.img_arr = img_arr
        self.frontier = []
        self.visited = []
        self.s_path = []
        self.path_cost = {}
        self.colors = [(0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)]
        
        self.pos = self.initial
        
        
    def actions(self, pos):
        x = pos[0]
        y = pos[1]
        #left, right, up, down
        actions = [(x-1, y), (x+1,y), (x, y-1), (x, y+1)]
        validos = [move for move in actions if self.isValid(move)]
        return validos
        
    
    def result(self, state, action):
        self.stepCost(action,state)
        self.visited.append(action)
        self.frontier.append(action)
    
    def goalTest(self, pos):
        return pos == self.goal

    def markPath(self, position, color):
        x,y = position
        self.img_arr[y][x] = list(color)
        
    def PathCost(self):
        self.s_path = []
        while self.pos != self.initial:
            self.s_path.append(self.pos)
            self.pos = self.path_cost[self.pos]
        self.s_path.append(self.initial)
        return self.s_path[::-1]

    
    def stepCost(self, state, action):
        self.path_cost[state] = action
        
    
    def isValid(self, pos):
        x = pos[0]
        y = pos[1]
        valid = False
        #Revisar que esté dentro de los parámetros de la imágen
        if (0<=x<len(self.img_arr[0]) and 0 <= y < len(self.img_arr)):
            valid = True      
        #Revisar si es una pared con color negro
            if (tuple(self.img_arr[y][x])==self.colors[0]):
                valid = False
            
        return valid
    
    
                
            
            