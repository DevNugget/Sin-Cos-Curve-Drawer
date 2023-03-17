import math
import sys

graph = {
    "3" :[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "2" :[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "1" :[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "0" :['-','-','-','-','-','-','-','-','-','-','-','-','-'],
    "-1":[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "-2":[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "-3":[' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' '],
    "-4":[' ','(','-',')','.','(','+',')',' ',' ',' ',' ',' '],
    "v1":[ 3 , 2 , 1 , 9 , 0 , 9 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
    "v2":[ 6 , 7 , 8 , 0 ,' ', 0 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ],
    "v3":[ 0 , 0 , 0 ,' ',' ',' ', 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
}

def blit_graph():
    for row in graph.values():
        print(*row)

def set_coords():
    graph_type = ""
    theta_multiplier = 1
    theta_power = 1
    
    if len(sys.argv) > 1:
        graph_type = sys.argv[1]
        if len(sys.argv) > 2:
            if sys.argv[2] == "-arg":
                theta_multiplier = int(sys.argv[3])
                theta_power = int(sys.argv[4])
    else:
        print("Error: no graph type (sin/cos) specified.")
        quit()
    
    x_shift = 0
    for i in range(-360, 810, 90):
        if graph_type == "sin":
            y_value = int(theta_multiplier*(math.sin(math.radians(i)))**theta_power)
        elif graph_type == "cos":
            y_value = int(theta_multiplier*(math.cos(math.radians(i)))**theta_power)
    
        graph[str(y_value)][x_shift] = '#'
        x_shift += 1
        
set_coords()
blit_graph()
