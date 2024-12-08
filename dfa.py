import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx

def validate_string():
    try:
        states = int(entry_states.get())
        start_state = entry_start_state.get()
        accepting_states = entry_accepting_states.get().split(',')
        transitions = entry_transitions.get().split(';')
        input_string = entry_input_string.get()

        # Build the transition dictionary
        transition_dict = {}
        for t in transitions:
            src, symbol, dest = t.split(',')
            if (src, symbol) not in transition_dict:
                transition_dict[(src, symbol)] = dest

        # Simulate the DFSM
        current_state = start_state
        for symbol in input_string:
            if (current_state, symbol) in transition_dict:
                current_state = transition_dict[(current_state, symbol)]
            else:
                result.set("Rejected")
                return

        result.set("Accepted" if current_state in accepting_states else "Rejected")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def draw_graph():
    G = nx.DiGraph()
    transitions = entry_transitions.get().split(';')
    for t in transitions:
        src, symbol, dest = t.split(',')
        G.add_edge(src, dest, label=symbol)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.show()

# GUI Layout
root = tk.Tk()
root.title("DFSM Simulator")

tk.Label(root, text="Number of States:").grid(row=0, column=0)
entry_states = tk.Entry(root)
entry_states.grid(row=0, column=1)

tk.Label(root, text="Start State:").grid(row=1, column=0)
entry_start_state = tk.Entry(root)
entry_start_state.grid(row=1, column=1)

tk.Label(root, text="Accepting States (comma-separated):").grid(row=2, column=0)
entry_accepting_states = tk.Entry(root)
entry_accepting_states.grid(row=2, column=1)

tk.Label(root, text="Transitions (src,symbol,dest;...):").grid(row=3, column=0)
entry_transitions = tk.Entry(root)
entry_transitions.grid(row=3, column=1)

tk.Label(root, text="Input String:").grid(row=4, column=0)
entry_input_string = tk.Entry(root)
entry_input_string.grid(row=4, column=1)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=5, column=0)
tk.Label(root, textvariable=result).grid(row=5, column=1)

tk.Button(root, text="Validate String", command=validate_string).grid(row=6, column=0)
tk.Button(root, text="Show Diagram", command=draw_graph).grid(row=6, column=1)

root.mainloop()
