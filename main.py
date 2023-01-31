from PIL import Image
import numpy as np
from Framework import FrameWork

img_path = "img/resize_tur_test.bmp"
img_path2 = "img/probando1.bmp"
def RemoveChoice(problem, option):
    if option==0:
        return problem.frontier.pop(0)
    elif option == 1:
        return problem.frontier.pop()

    elif option == 2:
        minimo = min(problem.frontier, key=lambda x: h(problem, x))
        index = problem.frontier.index(minimo)
        return problem.frontier.pop(index)

def h(problem, value):
    return round(((value[0] - problem.goal[0])**2 + (value[1] - problem.goal[1])**2)**0.5)


def graph_search(problem,algorithm):
    
    problem.path_cost[problem.initial] = None
    problem.frontier.append(problem.initial)
    problem.visited.append(problem.initial)
    
    while problem.frontier:
        problem.pos = RemoveChoice(problem, algorithm)
        if problem.goalTest(problem.pos):
            print("Goal Found")
            return problem.PathCost()
        
        for position in problem.actions(problem.pos):
            if position not in problem.visited:
                problem.result(problem.pos, position)
                               


def GetData(imagen):
    img = Image.open(imagen)
    img_arr = np.array(img)
    goals = []
    
    for x in range(len(img_arr)):
        for y in range(len(img_arr[x])):
            if tuple(img_arr[y][x])==(255,0,0):
                ini = (x,y)
            elif tuple(img_arr[y][x])==(0,255,0):
                goals.append((x,y))
    return (ini,goals[-1],img_arr)



def Solution(algorithm):
    ini, goal, img_arr = GetData(img_path2)
    problem = FrameWork(ini,goal,img_arr)
    
    path = graph_search(problem, algorithm)

    if path:
        path.pop()
        path.pop(0)
        for pos in path:
            problem.markPath(pos,(0,0,255))

    
    ima = problem.img_arr
    ima = Image.fromarray(ima)
    
    ima.save("img/solution"+str(algorithm)+".bmp")

Solution(0) #Breadth-first
Solution(1) #Depth-First
Solution(2) #A*


    
    