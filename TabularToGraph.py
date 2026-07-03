import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# =====================================================================
# STEP 1: Build the tabular data BY HAND
# ---------------------------------------------------------------------
# Real transaction data lives in a table (CSV/Excel). We're typing a
# small one so you can SEE every node and edge that comes out of it.
# Each row = ONE money transfer = ONE edge in our graph.
#   sender   -> the SOURCE node (money leaves here)
#   receiver -> the TARGET node (money arrives here)
#   amount, date -> EDGE attributes (extra info about that transfer)
# =====================================================================
transactions = [
    {"sender": "Alice",  "receiver": "Bob",    "amount": 50,  "date": "2026-07-01"},
    {"sender": "Alice",  "receiver": "Carol",  "amount": 20,  "date": "2026-07-01"},
    {"sender": "Bob",    "receiver": "Carol",  "amount": 75,  "date": "2026-07-02"},
    {"sender": "Carol",  "receiver": "Dave",   "amount": 30,  "date": "2026-07-02"},
    {"sender": "Dave",   "receiver": "Erin",   "amount": 90,  "date": "2026-07-03"},

    # ---- a suspicious "fraud ring": money loops back to where it started ----
    {"sender": "Frank",  "receiver": "Grace",  "amount": 500, "date": "2026-07-03"},
    {"sender": "Grace",  "receiver": "Heidi",  "amount": 500, "date": "2026-07-03"},
    {"sender": "Heidi",  "receiver": "Frank",  "amount": 500, "date": "2026-07-04"},
]

df = pd.DataFrame(transactions)
print("=== The table (DataFrame) ===")
print(df)
print()

# =====================================================================
# STEP 2: Turn the table into a GRAPH
# ---------------------------------------------------------------------
# This ONE function replaces all the hand-typed add_edges_from() you
# were doing before. NetworkX reads the columns you point it at:
#   - it makes an edge for every row
#   - it AUTO-CREATES the nodes from the unique names it sees
#   - create_using=DiGraph() -> directed, because money has a direction
# =====================================================================
G = nx.from_pandas_edgelist(
    df,
    source="sender",
    target="receiver",
    edge_attr=["amount", "date"],   # these columns get attached to each edge
    create_using=nx.DiGraph()       # DiGraph = arrows; use nx.Graph() for no direction
)

print("=== What NetworkX built ===")
print("Nodes (auto-created):", list(G.nodes()))
print("Number of edges     :", G.number_of_edges())
print("One edge's data      :", G["Alice"]["Bob"])   # -> {'amount': 50, 'date': ...}
print()

# =====================================================================
# STEP 3: ASK THE GRAPH QUESTIONS (this is why we bothered!)
# ---------------------------------------------------------------------
# A table can't easily answer these; a graph can.
# =====================================================================

# 3a) Who receives from the most different people? (in-degree)
print("In-degree (how many people paid each person):")
for person, deg in sorted(G.in_degree(), key=lambda x: -x[1]):
    print(f"   {person}: {deg}")
print()

# 3b) THE PAYOFF: find money that loops back to its origin (a ring).
#     simple_cycles walks the arrows and finds closed loops for you.
print("Suspicious cycles (money returning to its start):")
for cycle in nx.simple_cycles(G):
    print("   RING FOUND ->", " -> ".join(cycle), "->", cycle[0])
print()

# =====================================================================
# STEP 4: Draw it
# ---------------------------------------------------------------------
# Because nodes are auto-created, we no longer hand-write pos{}.
# spring_layout auto-positions them; seed keeps it repeatable.
# =====================================================================
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, with_labels=True,
    node_color="red", node_size=2500,
    font_color="white", font_size=12, font_weight="bold",
    width=2, arrowsize=20
)

# label each edge with its amount
edge_labels = nx.get_edge_attributes(G, "amount")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.margins(0.2)
plt.title("Money transfers as a graph")
plt.show()
