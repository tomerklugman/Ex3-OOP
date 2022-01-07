
# Ex3-OOP
# weighted directed graph


- creation of a graph data structure which contains: 
- nodes dictionary which contains <key,pos(x,y)> of node and looks like {key1:(x,y), key2:(x,y)..}
- edges nested dictionary which contains edges from nodes and looks like:
{srcNode1:{destNode:weight},{destNode:weight}..., srcNode2:{destNode,weight},...} 
each edge has (src,dest,weight)
- each graph has implemented algorithms used by Dijkstra's algorithm: 

1) save_to_json(filename), load_from_json(filename) - save and load json file 
2) shortest_path(src,dest) - find the shortest path and distance from source node to destination node and returns distance and path  
3) TSP(List cities) - find the cheapest weight from a chosen list of nodes
4) centerpoint(graph) - find node that has shortest distances to farthest nodes
5) plot_graph(graph) - draws graph if no node postion given points will be randomized
##### python implementation will be compared to java implementation execution speed in the wiki

-------------

### helpful Links

https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html 

https://www.geeksforgeeks.org/minimum-value-of-distance-of-farthest-node-in-a-graph/

https://www.interviewbit.com/blog/travelling-salesman-problem/

https://matplotlib.org/stable/tutorials/introductory/pyplot.html

----
### UML
![alt text](https://i.imgur.com/NuPSZvk.jpeg)
----
## requirements

required imports are:

matplotlib

numpy

pandas

----
## how to run
open Ex3.py file and change run("data/A5.json") to A0-A5 or T0 and run in interperter
```sh
run("data/A5.json") 
```

