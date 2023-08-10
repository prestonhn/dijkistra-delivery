# Box Delivery Using Dijstra Algoirthm

Python-based delivery optimization system for vans delivering boxes to designated coordinates. Uses Dijkstra’s algorithm for route optimization.

# Summary: 

In this project  we are delivering number of boxes on different locations using Dijikistra algorithm. Node class is representing each box with location(x coordinate, y coordinate). We are inserting those boxes in nodes_list

Once we have all list of boxes, we will send those list of boxes in creat_graph method. This method will initiate 2-d matrix in Graph object, calculates distance of each node from origin using distance formula and add those distance in matrix and after calculating each node distance it will return the graph. Then, the graph will send to Djikistra() and visit nodes on the base of short distance and in the end all visited list will be returned

In the end that route will be sent to Van object and van will deliver all boxes to that route

## Input
No of nodes with x coordinates and y coordinates
No of visited_nodes_names

## Output
Output will be in a text file with information that which box will deliver first on which location

# Running Project
"python main.py"
