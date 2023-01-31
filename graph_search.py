import numpy as np
from PIL import Image


class GraphSearch():
    def __init__(self, option, img):
        self.option = option
        self.img = img
        self.img_array = np.array(img)
        self.explored = []
        self.colors = [(0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)]
        self.initial = self.FindStart()
        
    def Search(self):
        print(self.initial)
    
    def FindStart(self):
        for y in range(len(self.img_array)):
            for x in range(len(self.img_array[y])):
                print(x,y,self.img_array[y][x])
                if tuple(self.img_array[y][x]) == self.colors[2]:
                    return (x,y)
                
    def GoalReached(self, position):
        return tuple(self.img_array[position[1][0]]) == self.colors[3]
    
    def Valid(self, position):
        return tuple(self.img_array[position[1][0]]) == self.colors[3]

    