import pydot
import os
print(os.getcwd())
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"
graph = pydot.Dot(graph_type="graph", rankdir = "LR")
colors = ['green','red']
core = "SQL Tuning"
Diag = ["Collect AWR,ASH,ADDM,OSWatcher,Execution plan"]
for D in Diag:
    graph.add_edge(pydot.Edge(core,D))
resource = ["CPU","IO","RAM","Network"]
for re in resource:
    graph.add_edge(pydot.Edge(Diag[0],re))

CPU = ["High Buffer Gets","Hard Parse","Parallel"]
for c in CPU:
    graph.add_edge(pydot.Edge(resource[0],c))
IO = ["DB file scattered reads","DB file sequential reads","Direct path read","Direct path write","Read by other session"]

RAM = ["Direct path read temp","Direct path write temp","Buffer busy waits","Latch","Library cache contention"]
for R in RAM:
    graph.add_edge(pydot.Edge(resource[2],R))

Network = ["sql*net more data from dblink","sql*net message from client","tcp socket (kgas)"]
for N in Network:
    graph.add_edge(pydot.Edge(resource[3],N))

for I in IO:
    graph.add_edge(pydot.Edge(resource[1],I))
f = open("SQL_Tuning.png","w")
graph.write_png("SQL_Tuning.png")
os.startfile("SQL_Tuning.png")
