import matplotlib.pyplot as plt
import networkx as nx


G=nx.Graph()

G.graph["Name"] = "My First Graph"

G.add_nodes_from([
    ("A",{"Age":19, "Gender":"F"}),
    ("B",{"Age":18, "Gender":"M"}),
    ("C",{"Age":22, "Gender":"M"}),
    ("D",{"Age":21, "Gender":"M"}),
    ("E",{"Age":20, "Gender":"F"}),
])  # for attributes of nodes-age&gender using a dictionary


# G.add_node("A", Age=19,gender="F")
# G.add_node("B", Age=118,gender="M")
# G.add_node("C", Age=22,gender="M")
# G.add_node("D", Age=21,gender="M")
# G.add_node("E", Age=20,gender="F")

G.add_edges_from([
    ("A","C",{"weight":1}),
    ("B","C",{"weight":0.5}),
    ("B","D", {"weight":0.6}),
    ("C","D",{"weight":0.8}),
    ("D","E",{"weight":1}),
])


# G.add_edge("A","C",weight=1)
# G.add_edge("B","C",weight=0.5)
# G.add_edge("C","D",weight=0.6)
# G.add_edge("D","D",weight=0.8)
# G.add_edge("E","E",weight=1)

pos={

    "A":(1,5),
    "B":(4.5,6.6),
    "C":(3.6,1.4),
    "D":(5.8,3.5),
    "E":(7.9,3.6)
}
#print(G.graph)
#print(G.nodes["C"])


nx.draw(G, pos=pos, with_labels=True, 
        node_color="red", node_size=3000,
        font_color="white",
        font_size=20, font_family="Times New Roman",
        width=5)
plt.margins(0.2)
plt.show()
