import tkinter as tk
import random
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

radius = 12;

def set_edge(node_value):
    global current_node_pos, node_to_pos
    canvas.unbind("<Button-1>")
    current_node = get_node(node_value)
    for pos in node_pos_list:
        if pos[0] == current_node:
            current_node_pos = pos[1]

    while True:
        node_to = input("Enter a node: ")
        if node_to.isalpha():  # Check if the input is a letter
            node_to = node_to.upper()  # Convert to uppercase
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
    # Offset the text up or down depending on the angle
    offset_distance = 15  # This is the distance from the line to the text
    text_offset_x = offset_distance * math.sin(angle)
    text_offset_y = offset_distance * -math.cos(angle)

    # If the line is mostly horizontal, adjust the text above/below the line
    if abs(angle) < math.pi / 4 or abs(angle) > 3 * math.pi / 4:
        mid_y += text_offset_y  # Adjusting text position above/below the line
    else:  # If the line is mostly vertical, adjust the text left/right
        mid_x += text_offset_x  # Adjusting text position left/right of the line

    # Display the distance
    canvas.create_text(mid_x, mid_y, text=str(user_input), fill="black")

    canvas.bind("<Button-1>", on_click)




g = Graph()

def calculate_edge_points(pos1, pos2, radius):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dist = math.sqrt(dx**2 + dy**2)
    dx /= dist
    dy /= dist

    # Calculate edge points on the circles
    start_x = pos1[0] + radius * dx
    start_y = pos1[1] + radius * dy
    end_x = pos2[0] - radius * dx
    end_y = pos2[1] - radius * dy

    return (start_x, start_y), (end_x, end_y)


def connect_all_nodes():
    for node1 in node_objects.keys():
        for node2 in node_objects.keys():
            if node1 != node2 and node2 not in [edge.node for edge in node_objects[node1]]:
                random_distance = random.randint(1, 10)
                node_objects[node1].append(Edge(random_distance, node2))
                node_objects[node2].append(Edge(random_distance, node1))

                # Draw the line and display the distance
                node1_pos = next(pos for n, pos in node_pos_list if n == node1)
                node2_pos = next(pos for n, pos in node_pos_list if n == node2)
                start_point, end_point = calculate_edge_points(node1_pos, node2_pos, radius)
                canvas.create_line(start_point, end_point, fill="black", width=2)
                mid_x = (node1_pos[0] + node2_pos[0]) / 2
                mid_y = (node1_pos[1] + node2_pos[1]) / 2
                angle = math.atan2(end_point[1] - start_point[1], end_point[0] - start_point[0])
                # Offset the text up or down depending on the angle
                offset_distance = 15  # This is the distance from the line to the text
                text_offset_x = offset_distance * math.sin(angle)
                text_offset_y = offset_distance * -math.cos(angle)

                # If the line is mostly horizontal, adjust the text above/below the line
                if abs(angle) < math.pi / 4 or abs(angle) > 3 * math.pi / 4:
                    mid_y += text_offset_y  # Adjusting text position above/below the line
                else:  # If the line is mostly vertical, adjust the text left/right
                    mid_x += text_offset_x  # Adjusting text position left/right of the line

                # Display the distance
                canvas.create_text(mid_x, mid_y, text=str(random_distance), fill="black")

def on_click(event):
    global node_count, node_names

    for node, (x, y) in node_pos_list:
        if (x - 12 <= event.x <= x + 12) and (y - 12 <= event.y <= y + 12):
            set_edge(node.value)
            return

    if node_count < len(node_names):


        node = Node(node_names[node_count])
        node_objects[node] = []  # Initialize with an empty list of edges

        x, y = event.x, event.y
        canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="red", outline="red")
        canvas.create_text(x,y, text=node_names[node_count], fill="black")
        node_count = node_count + 1
        node_pos = [event.x, event.y]
        node_pos_list.append((node, node_pos))
        # canvas.create_line(360, 540, event.x, event.y, fill="black", width=2)
    else:
        print("Node limit reached!")
        # print(node_pos_list)
        # print(str(node_objects[0])) 
        # for node in node_pos_list:
        #     for starter_pos in node_pos_list:
        #         canvas.create_line(starter_pos, node, fill="black", width=2)
        # get_node("A")
        #
        # print(node_A)


def find_shortest_path():
    print_node_objects()
    g.adjacency_list = node_objects
    starting_node = input("Sheno kulmin startues: ")

    dijkstra(g, get_node(starting_node))

def main():
    root = tk.Tk()
    root.title("Shto kulmet e grafit duke klikuar me maus.")

    window_width = 600
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    # Create a frame for the canvas
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(side=tk.TOP)

    global canvas
    canvas = tk.Canvas(canvas_frame, width=window_width, height=window_height, bg="white")
    canvas.pack()

    # Create a frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT)

    button2 = tk.Button(button_frame, text="FIND PATH", command=find_shortest_path)
    button2.pack(side=tk.LEFT, padx=5, pady=5)

    connect_all_button = tk.Button(button_frame, text="CONNECT ALL", command=connect_all_nodes)
    connect_all_button.pack(side=tk.LEFT, padx=5, pady=5)

    canvas.bind("<Button-1>", on_click)

    root.mainloop()

def print_node_objects(): #this method prints the all the nodes in node_objects and the edges for each node(edges are printed under the node as (distance, node) tuples)
    for node, edges in node_objects.items():
        print(f"Node {node}")
        for edge in edges:
            print(edge)

if __name__ == "__main__":
    main()



