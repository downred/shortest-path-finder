import tkinter as tk
import math

from dijkstra import dijkstra
from graph import Graph, Node, Edge

def get_node(node_value):
    for node in node_objects.keys():
        if node.value == node_value:
            return node

node_count=0
node_names="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

node_pos_list = []
node_pos = []
node_objects = {}

radius = 12

def set_edge(node_value):
    global current_node_pos, node_to_pos
    canvas.unbind("<Button-1>")
    current_node = get_node(node_value)
    for pos in node_pos_list:
        if pos[0] == current_node:
            current_node_pos = pos[1]

    while True:
        node_to = input("Enter a node: ")
        if node_to.isalpha():  
            node_to = node_to.upper()  
            node_to = get_node(node_to)
            break
        else:
            print("Invalid input. Please enter a letter for the node.")

    while True:
        try:
            user_input = int(input("Enter the edge distance: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the edge distance.")

    for pos in node_pos_list:
        if pos[0] == node_to:
            node_to_pos = pos[1]

    node_objects[current_node].append(Edge(user_input, node_to))
    node_objects[node_to].append(Edge(user_input, current_node))

    current_node_pos = next(pos for n, pos in node_pos_list if n == current_node)
    node_to_pos = next(pos for n, pos in node_pos_list if n == node_to)
    start_point, end_point = calculate_edge_points(current_node_pos, node_to_pos, radius)
    canvas.create_line(start_point, end_point, fill="black", width=2)
    mid_x = (current_node_pos[0] + node_to_pos[0]) / 2
    mid_y = (current_node_pos[1] + node_to_pos[1]) / 2
    angle = math.atan2(end_point[1] - start_point[1], end_point[0] - start_point[0])
    
    offset_distance = 15  
    text_offset_x = offset_distance * math.sin(angle)
    text_offset_y = offset_distance * -math.cos(angle)

    
    if abs(angle) < math.pi / 4 or abs(angle) > 3 * math.pi / 4:
        mid_y += text_offset_y  
    else:  
        mid_x += text_offset_x  

    
    canvas.create_text(mid_x, mid_y, text=str(user_input), fill="black")

    canvas.bind("<Button-1>", on_click)




g = Graph()

def calculate_edge_points(pos1, pos2, radius):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dist = math.sqrt(dx**2 + dy**2)
    dx /= dist
    dy /= dist

    
    start_x = pos1[0] + radius * dx
    start_y = pos1[1] + radius * dy
    end_x = pos2[0] - radius * dx
    end_y = pos2[1] - radius * dy

    return (start_x, start_y), (end_x, end_y)

def on_click(event):
    global node_count, node_names

    for node, (x, y) in node_pos_list:
        if (x - 12 <= event.x <= x + 12) and (y - 12 <= event.y <= y + 12):
            set_edge(node.value)
            return

    if node_count < len(node_names):


        node = Node(node_names[node_count])
        node_objects[node] = []  

        x, y = event.x, event.y
        canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="red", outline="red")
        canvas.create_text(x,y, text=node_names[node_count], fill="black")
        node_count = node_count + 1
        node_pos = [event.x, event.y]
        node_pos_list.append((node, node_pos))
        
    else:
        print("Node limit reached!")
        
        
        
        
        
        
        
        


def find_shortest_path():
    print_node_objects()
    g.adjacency_list = node_objects
    starting_node = input("Sheno kulmin startues: ")

    dijkstra(g, get_node(starting_node))

def main():
    root = tk.Tk()
    root.title("Shto kulmet e grafit duke klikuar me maus.")

    window_width = 600
    window_height = 650  

    
    root.geometry(f"{window_width}x{window_height}")

    
    root.minsize(window_width, window_height)

    
    button_frame = tk.Frame(root)
    
    button_frame.pack(side=tk.TOP, fill=tk.X, pady=(5, 0))  

    button2 = tk.Button(button_frame, text="FIND PATH", command=find_shortest_path)
    button2.pack(side=tk.LEFT, padx=5, pady=5)

    
    canvas_frame = tk.Frame(root)
    
    canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(5, 0))  

    global canvas
    
    canvas_height = window_height - 50  
    canvas = tk.Canvas(canvas_frame, width=window_width, height=canvas_height, bg="white")
    
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.bind("<Button-1>", on_click)

    root.mainloop()


def print_node_objects(): 
    for node, edges in node_objects.items():
        print(f"Node {node}")
        for edge in edges:
            print(edge)

if __name__ == "__main__":
    main()



