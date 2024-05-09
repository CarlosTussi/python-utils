#Structure containing information about a vertex from a graph
class Vertex():

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return str(self.label)

#List that contains all the vertices from a graph
class Graph():
    def __init__(self):
        self.vertices = []
        self.adjacencyMatrix = {}
    
    def __str__(self):
        graph_Str = ""
        for vertex in self.vertices:
            graph_Str += str(vertex) + ": "
            for i in self.vertices:
                if((vertex.label, i.label) in self.adjacencyMatrix):
                    graph_Str += f"({vertex}-{i}) "
            graph_Str += "\n"


        return graph_Str

    def addVertex(self, vertex):
        self.vertices.append(vertex)
    
    def addEdge(self, v1, v2):
        self.adjacencyMatrix[(v1.label, v2.label)] = True
        self.adjacencyMatrix[(v2.label, v1.label)] = True

    def findNeighbours(self, vertex):
        neighbours = []

        for elem in self.vertices:
            if (vertex.label, elem.label) in self.adjacencyMatrix:
                neighbours.append(elem)
        
        return neighbours

    def depthFirstTraversal(self, vertex = None, visited = set()):
        if not vertex:
            vertex = self.vertices[0]   #Start with the first vertex from the list
        
        ####################
        # VISIT THE VERTEX #
        ####################
        visited.add(vertex)
        print(str(vertex) + " visited")
            
        neighbours = self.findNeighbours(vertex)      #Get the neighbours of current node

        #For each neighbour
        for neighbour in neighbours:
            #If not yet visited, recursion
            if neighbour not in visited:
                #visited.append(neighbour)  #Visit the node
                self.depthFirstTraversal(neighbour, visited)    #Recursion with its neighbours


    def depthFirstSearch(self, target = None, vertex = None, visited = set()):
        if not vertex:
            vertex = self.vertices[0]   #Start with the first vertex from the list

        ####################
        # VISIT THE VERTEX #
        ####################
        visited.add(vertex)
        print("Visited: " + str(vertex.label))

        if (target == vertex.label):
            return True
        else:
            neighbours = self.findNeighbours(vertex)      #Get the neighbours of current node
             #For each neighbour
            for neighbour in neighbours:
                #If not yet visited, recursion
                if neighbour not in visited:
                    #visited.append(neighbour)  #Visit the node
                    if(self.depthFirstSearch(target, neighbour, visited)):   #Recursion with its neighbours
                        return True


        return False

    def minimumSpanningTree(self):
        #Sort all the edges (if weighted)
        #Inizialize empty set to contain MST
        #Iterate through the sorted edges
            #If it does not create a cycle, add to the set
        
        pass


if __name__ == "__main__":
    #listVertices = [Vertex(i) for i  in  range(10)]
    listVertices = {"A":Vertex("A"), "B":Vertex("B"), "C":Vertex("C"), "D":Vertex("D"), "E":Vertex("E")}
    graph_deux = {"A":Vertex("A"), "B":Vertex("B"), "C":Vertex("C"), "D":Vertex("D"), "E":Vertex("E"), "F":Vertex("F"), "G":Vertex("G"), "H":Vertex("H"), "I":Vertex("I")}
    myGraph = Graph()
    mySecondGraph = Graph()

    for key in listVertices:
        myGraph.addVertex(listVertices[key])


    myGraph.addEdge(listVertices["A"], listVertices["B"])
    myGraph.addEdge(listVertices["A"], listVertices["C"])
    myGraph.addEdge(listVertices["C"], listVertices["B"])
    myGraph.addEdge(listVertices["B"], listVertices["E"])
    myGraph.addEdge(listVertices["C"], listVertices["E"])
    myGraph.addEdge(listVertices["B"], listVertices["D"])


    for key in graph_deux:
        mySecondGraph.addVertex(graph_deux[key])

    mySecondGraph.addEdge(graph_deux["A"],graph_deux["B"])
    mySecondGraph.addEdge(graph_deux["A"],graph_deux["C"])
    mySecondGraph.addEdge(graph_deux["A"],graph_deux["D"])
    mySecondGraph.addEdge(graph_deux["A"],graph_deux["E"])
    mySecondGraph.addEdge(graph_deux["B"],graph_deux["F"])
    mySecondGraph.addEdge(graph_deux["F"],graph_deux["H"])
    mySecondGraph.addEdge(graph_deux["D"],graph_deux["G"])
    mySecondGraph.addEdge(graph_deux["G"],graph_deux["I"])

    print(myGraph)
    print(mySecondGraph)


    mySecondGraph.depthFirstTraversal()
    print(mySecondGraph.depthFirstSearch("G"))