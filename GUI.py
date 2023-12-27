import tkinter as tk
from graph import Graph, Node, Edge

def get_node(node_value):
    for node in node_objects.keys():
        if node.value == node_value:
            print(f"Found node {node} at target position")
            break


node_count=0
node_names="ABCD"

node_pos_list = []
node_pos = []
node_objects = {}

g = Graph()

def on_click(event):
    global node_count, node_names

    if node_count < len(node_names):


        node = Node(node_names[node_count])
        node_objects[node] = []  # Initialize with an empty list of edges

        x, y = event.x, event.y
        canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="red", outline="red")
        canvas.create_text(x,y, text=node_names[node_count], fill="black")
        node_count = node_count + 1
        node_pos = [event.x, event.y]
        node_pos_list.append(node_pos)
        # canvas.create_line(360, 540, event.x, event.y, fill="black", width=2)
    else:
        print("Node limit reached!")
        # print(node_pos_list)
        # print(str(node_objects[0])) 
        for node in node_pos_list:
            for starter_pos in node_pos_list:
                canvas.create_line(starter_pos, node, fill="black", width=2)
        get_node("A")

        # print(node_A)


def main():
    root = tk.Tk()
    root.title("Click to place a node")

    window_width = 500
    window_height = 500
    root.geometry(f"{window_width}x{window_height}")

    global canvas
    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.pack()

    canvas.bind("<Button-1>", on_click)

    root.mainloop()

if __name__ == "__main__":
    main()

