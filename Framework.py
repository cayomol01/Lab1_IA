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
        
        
    def actions(self, pos):
        x = pos[0]
        y = pos[1]
        #left, right, up, down
        actions = [(x-1, y), (x+1,y), (x, y-1), (x, y+1)]
        validos = [move for move in actions if self.isValid(move)]
        return validos
        
    
    def result(self, state, action):
        pass
    
    def goalTest(self, pos):
        x = pos[0]
        y = pos[1]
        return tuple(self.img_arr[y][x]) == self.colors[3]

            
    
    def stepCost(self, state, action):
        self.pCost[action] = state
        
    
    def isValid(self, pos):
        x = pos[0]
        y = pos[0]
        valid = False
        
        #Revisar que esté dentro de los parámetros de la imágen
        if (0<=x<self.img.width and 0 <= y < self.img.height):
            valid = True      
        #Revisar si es una pared con color negro
            if (tuple(self.img_arr[y][x])==self.colors[0]):
                valid = False
            
        return valid
    
                
            
            