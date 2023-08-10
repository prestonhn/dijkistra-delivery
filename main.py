import numpy as np
import math 

class Goods:
  def __init__(self, name, no_of_boxes, quantity_per_box):
    self.name = name
    self.no_of_boxes = no_of_boxes
    self.quantity_per_box = quantity_per_box

class Node:
  def __init__(self ,name, x_coordinate , y_coordinate):
     self.name = name
     self.x_coordinate = x_coordinate 
     self.y_coordinate = y_coordinate

class Graph:
  def __init__(self , no_of_nodes):
     self.nodes_matrix = np.empty( [no_of_nodes+1, no_of_nodes+1] , dtype=object )
  
  def compute_distance(self,node1 , node2):
    x = node2.x_coordinate - node1.x_coordinate
    x = x*x
    y = node2.y_coordinate - node1.y_coordinate
    y = y*y
    return  math.sqrt(x+y)

class Van:
  def __init__(self,delivery_id,no_of_deliveries,goods,color,route):
    self.delivery_id = delivery_id
    self.no_of_deliveries = no_of_deliveries
    self.goods = goods
    self.color = color
    self.route = route

def create_graph(nodes_list):
  #Create Graph
  graph = Graph(len(nodes_list))
  #giving titles to matrix rows and columns
  graph.nodes_matrix[0][0] = "-"
  for i in range(1,len(nodes_list)+1):
    graph.nodes_matrix[0][i] = "node"+str(i)
    graph.nodes_matrix[i][0] = "node"+str(i)
  #assigning distances to matrix
  for i in range(0,len(nodes_list)):
    node1 = nodes_list[i]
    for j in range(0,len(nodes_list)):
      node2 = nodes_list[j]
      distance = graph.compute_distance(node2,node1)
      str_distance = str("{:.2f}".format(distance))
      graph.nodes_matrix[i+1][j+1] = str_distance
  return graph

def Djikistra(nodes,graph):
  visited_nodes = []
  visited_nodes_names = []
  s = graph.nodes_matrix[1][1]
  visited_nodes.append(nodes[0])
  visited_nodes_names.append("node1")
  row = 1
  col_count = 1
  for r in range(0,len(nodes)-1):
    shortest_distance = 1000000
    for col in range(1,len(nodes)+1):
      if(row==col):
        shortest_distance = shortest_distance + 0
      else:
        if(graph.nodes_matrix[0][col] in visited_nodes_names):
          shortest_distance = shortest_distance + 0
        else:
          if(shortest_distance>float(graph.nodes_matrix[row][col])):
            shortest_distance = float(graph.nodes_matrix[row][col])
            col_count = col
          else:
            continue
    visited_nodes.append(nodes[col_count-1])
    visited_nodes_names.append(nodes[col_count-1].name)
    row = col_count
  return visited_nodes

def output(van):
  f = open(f"van{van.delivery_id}.txt", "w")
  f.write(f"Delivery {van.color} nodes \n")
  f.write(f"Delivery Id {van.delivery_id} \n")
  f.write(f"No of Deliveries:{van.no_of_deliveries}\n")
  f.write(f"*Delivery number {van.delivery_id} co-ordinates are*\n")
  f.write(f"                          Delivery Co-ordinates\n")
  f.write(f"Delivery number(node)     X               Y               \n")
  for i in range(1,len(van.route)):
    f.write(f"{i}                         {van.route[i].x_coordinate}               {van.route[i].y_coordinate}               \n")
  f.write("\n")
  f.write(f"Boxes on van:{van.no_of_deliveries} (1 Box per delivery)")
  f.write(f"Each box has 2 meals inside")
  f.write("\n")
  f.write(f"Goods on Van     Delivery ID     Boxes on Van     Product QTY\n")
  total_boxes = 0
  total_products = 0
  for i in range(len(van.goods)):
    f.write(f"{van.goods[i].name}       {van.delivery_id}                    {van.goods[i].no_of_boxes}                 {van.goods[i].quantity_per_box}\n")
    total_boxes = total_boxes + van.goods[i].no_of_boxes
    total_products =  total_products + van.goods[i].no_of_boxes*2
  f.write(f"                  Total                {total_boxes}                {total_products}\n")
  f.close()

def main():
    goods_list = []
    goods_list.insert(0,Goods("Protein Meal",5,2))
    goods_list.insert(1,Goods("Weight Meal",5,2))
    goods_list.insert(2,Goods("Health Meal",3,2))
    
    #create nodes list and add those to graph
    nodes_list = []
    nodes_list.insert(0,(Node("node1" , 0 , 0)))
    nodes_list.insert(1,(Node("node2" , 0 , 4)))
    nodes_list.insert(2,(Node("node3" , 1 , 1)))
    nodes_list.insert(3,(Node("node4" , 2 , 0)))
    nodes_list.insert(4,(Node("node5" , 4 , 4)))
    nodes_list.insert(5,(Node("node6" , 7 , 3)))
    nodes_list.insert(6,(Node("node7" , -3 , 2)))
    nodes_list.insert(7,(Node("node8" , -4 , 6)))
    nodes_list.insert(8,(Node("node9" , -3 , -1)))
    nodes_list.insert(9,(Node("node10" , -5 , -1)))
    nodes_list.insert(10,(Node("node11" , -2 , -3)))
    nodes_list.insert(11,(Node("node12" , 0 , -5)))
    nodes_list.insert(12,(Node("node13" , 2 , -3)))
    nodes_list.insert(13,(Node("node14" , 4 , -2)))

    #creat graph
    graph1 = create_graph(nodes_list)
    route = Djikistra(nodes_list,graph1)
    #creating van object with route 
    no_of_deliveries = 0
    for i in range(0,len(goods_list)):
      no_of_deliveries = no_of_deliveries + goods_list[i].no_of_boxes
    van1 = Van(1,no_of_deliveries,goods_list,"Green",route)
    output(van1)

    #now for orange van
    goods_list2 = []
    goods_list2.insert(0,Goods("Protein Meal",4,2))
    goods_list2.insert(1,Goods("Weight Meal",4,2))
    goods_list2.insert(2,Goods("Health Meal",3,2))
    #create nodes list and add those to graph
    nodes_list2 = []
    nodes_list2.insert(0,(Node("node1" , 0 , 0)))
    nodes_list2.insert(1,(Node("node2" , 3 , 1)))
    nodes_list2.insert(2,(Node("node3" , 6 , 2)))
    nodes_list2.insert(3,(Node("node4" , 6 , 6)))
    nodes_list2.insert(4,(Node("node5" , 2 , 6)))
    nodes_list2.insert(5,(Node("node6" , -2 , 0)))
    nodes_list2.insert(6,(Node("node7" , -5 , 1)))
    nodes_list2.insert(7,(Node("node8" , -5 , 4)))
    nodes_list2.insert(8,(Node("node9" , 0 , -2)))
    nodes_list2.insert(9,(Node("node10" , -3 , -5)))
    nodes_list2.insert(10,(Node("node11" , 2 , -2)))
    nodes_list2.insert(11,(Node("node12" , 6 , -4)))
    #creat graph
    graph2 = create_graph(nodes_list2)
    route = Djikistra(nodes_list2,graph2)
    #creating van object with route 
    no_of_deliveries = 0
    for i in range(0,len(goods_list2)):
      no_of_deliveries = no_of_deliveries + goods_list2[i].no_of_boxes
    van2 = Van(2,no_of_deliveries,goods_list2,"Orange",route)
    output(van2)

if __name__ == "__main__":
    main()