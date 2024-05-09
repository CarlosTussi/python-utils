"""
[Class Vetex]

- Represent a vertex from a graph

    Attributes:
    -----------
        label: label that identifies the vertex
        data: data associated with the vertexù

    Method:
    -------
        getData: return the associated data with the vertex
"""
class Vertex():

    def __init__(self, label, data = None):
        self.label = label
        self.data = data

    def __str__(self):
        return str(self.label)

    """
    getData()

    Returns the associated data with the vertex

        Input
        -----
            None
        
        Output:
        ------
            data : any
    """
    def getData(self) -> any:
        return self.data

"""
[Class Graph]

- Represent a Graph with vertices

    Attributes:
    ----------
        vertices : [Vertex]
            - Represent a list of vertices
        
        adjacentMatrix : dict
            - Dictionary/hash table representing the adjacent matrix (edges)
    
    Methods:
    -------
        addVertex : add a vertex to the graph
        addEdge: add an edge between two vertices
        findNeighbours: find the neighbours of a vertix
        depthFirstTraversal: traverse in a deapth first fashion
        depthFirstSearch: search for vertex in a DFS fashion
        minimunSpanningTree: find a minimum spanning tree for the graph

"""
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

    """
    addVertex()

    - Add a vertex to the graph
    
        Input:
        ------
            vertex: Vertex()

        Output:
        ------
            None
    """
    def addVertex(self, vertex : Vertex) -> None:
        self.vertices.append(vertex)
    


    """
    addEdge()

    -Add an edge between two vertices (v1 and v2)

        Input:
        ------
            v1: Vertex
            v2: Vertex

        Output:
        -------
            None
    """
    def addEdge(self, v1 : Vertex, v2 : Vertex) -> None:
        self.adjacencyMatrix[(v1.label, v2.label)] = True
        self.adjacencyMatrix[(v2.label, v1.label)] = True

    """
    findNeighbours()

    - Finds a list of all the neighbours of a given vertex

        Input:
        -----
            vertex: Vertex

        Output:
        -------
            neighbours : [Vertex]

    """
    def findNeighbours(self, vertex : Vertex) -> list:
        neighbours = []

        for elem in self.vertices:
            if (vertex.label, elem.label) in self.adjacencyMatrix:
                neighbours.append(elem)
        
        return neighbours


    """
    [Recursive]
    depthFirstTraversal()


    -Traverse the graph in a DFS fashion.   

        Input:
        ------
            vertex: Vertex
            visited: set()

        Output:
        -------     
            None

    """
    def depthFirstTraversal(self, vertex : Vertex = None, visited = set()) -> None:
        if not vertex:
            vertex = self.vertices[0]   #Start the seaerch with the first vertex from the list
        
        visited.add(vertex)             #Visits the vertex
        print(str(vertex) + " visited")
            
        neighbours = self.findNeighbours(vertex)      #Get the neighbours of current vertex
        for neighbour in neighbours:               #For each neighbour
            if neighbour not in visited:           #If neighbour not yet visited
                self.depthFirstTraversal(neighbour, visited)    #Check their neighbours

    """
    [Recursive]
    depthFirstSearch()


    -Perform a DFS for a target on the graph. 

        Input:
        ------
            target: Vertex
            vertex: Vertex
            visited: set()

        Output:
        -------     
            True/False : bool
    
    """
    def depthFirstSearch(self, target : Vertex, vertex : Vertex = None, visited = set()) -> bool:
        if not vertex:
            vertex = self.vertices[0]   #Start with the first vertex from the list

        visited.add(vertex)              #Visits the vertex
        print("Visited: " + str(vertex.label))

        if (target == vertex.label):    #If target vertex is found
            return True
        else:                           #If not found, check its neighbours
            neighbours = self.findNeighbours(vertex)      #Get the neighbours of current node
            for neighbour in neighbours:                  #For each neighbour
                if neighbour not in visited:              #If neighbour not yet visited
                    if(self.depthFirstSearch(target, neighbour, visited)):   #If  found  the target checking current vertex's neighbouts, return true
                        return True


        return False        #If target was not found in the current vertex's neighbours

    """
    [Recursive]
    minimumSpanningTree()

    - Find one possible MST from the graph using this methods

        Input:
        ------
            vertex: Vertex
            visited: set()
            MST: Graph()
        
        Output:
        -------
            MST : Graph()

    """
    def minimumSpanningTree(self, vertex : Vertex = None, visited = set(), MST = None):
        if(not MST):
            MST = Graph()

        if not vertex:
            vertex = self.vertices[0]   #Start the seaerch with the first vertex from the list
        
        visited.add(vertex)             #Visits the vertex
        MST.vertices.append(vertex)
        print(str(vertex) + " visited")
            
        neighbours = self.findNeighbours(vertex)      #Get the neighbours of current vertex
        for neighbour in neighbours:               #For each neighbour
            if neighbour not in visited:           #If neighbour not yet visited
                MST.adjacencyMatrix[(vertex.label, neighbour.label)] = True             #Add a new edge to the MST
                MST.adjacencyMatrix[(neighbour.label),vertex.label] = True
                self.minimumSpanningTree(neighbour, visited, MST)    #Check their neighbours


        return MST


if __name__ == "__main__":

    #Graph test 1
    graph_un_vertices = {"A":Vertex("A"), "B":Vertex("B"), "C":Vertex("C"), "D":Vertex("D"), "E":Vertex("E")}
    graph_un = Graph()

    for key in graph_un_vertices:
        graph_un.addVertex(graph_un_vertices[key])

    graph_un.addEdge(graph_un_vertices["A"], graph_un_vertices["B"])
    graph_un.addEdge(graph_un_vertices["A"], graph_un_vertices["C"])
    graph_un.addEdge(graph_un_vertices["C"], graph_un_vertices["B"])
    graph_un.addEdge(graph_un_vertices["B"], graph_un_vertices["E"])
    graph_un.addEdge(graph_un_vertices["C"], graph_un_vertices["E"])
    graph_un.addEdge(graph_un_vertices["B"], graph_un_vertices["D"])

    print(graph_un)


    #Graph Test 2
    graph_deux_vertices = {"A":Vertex("A"), "B":Vertex("B"), "C":Vertex("C"), "D":Vertex("D"), "E":Vertex("E"), "F":Vertex("F"), "G":Vertex("G"), "H":Vertex("H"), "I":Vertex("I")}
    graph_deux = Graph()

    for key in graph_deux_vertices:
        graph_deux.addVertex(graph_deux_vertices[key])

    graph_deux.addEdge(graph_deux_vertices["A"],graph_deux_vertices["B"])
    graph_deux.addEdge(graph_deux_vertices["A"],graph_deux_vertices["C"])
    graph_deux.addEdge(graph_deux_vertices["A"],graph_deux_vertices["D"])
    graph_deux.addEdge(graph_deux_vertices["A"],graph_deux_vertices["E"])
    graph_deux.addEdge(graph_deux_vertices["B"],graph_deux_vertices["F"])
    graph_deux.addEdge(graph_deux_vertices["F"],graph_deux_vertices["H"])
    graph_deux.addEdge(graph_deux_vertices["D"],graph_deux_vertices["G"])
    graph_deux.addEdge(graph_deux_vertices["G"],graph_deux_vertices["I"])

    print(graph_deux)
    graph_deux.depthFirstTraversal()
    print(graph_deux.depthFirstSearch("G"))


    new_mst = graph_deux.minimumSpanningTree()
    print(new_mst)