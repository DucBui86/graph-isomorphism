from graph import Graph, Vertex, Edge
from graph_io import load_graph


def basic_colorref(path):
    # Read the graph from the file
    with open(path, "r") as file:
        graphs = load_graph(file, read_list=True)
    
    colour_list = []   # Initialize an empty list for storing colour sets
    iteration_count = [0]*len(graphs[0])   # Initialize iteration count for this graph
    max_colour = 0    
    
    # initial color mapping
    for index, graph in enumerate(graphs[0]):
        for vertex in graph.vertices:
            vertex.label = vertex.degree    # set the initial colour of the vertex to its degree
            max_colour = max(vertex.label, max_colour)  # update the max number of the colour value
            colour_list.append(set([vertex.label for vertex in graph.vertices])) # add the colour to the list to check the stability of the colour set
        iteration_count[index] = 1
        
        
    num_colour = [0] 
    while True:
        num_colour = [len(colour) for colour in colour_list]   
        colour_dict: dict[tuple[int: "neighbor_colour"], int: "vertex_colour"] = {}
        for index, graph in enumerate(graphs[0]):
            new_dict: dict[Vertex: "vertex", int: "new_colour"] = {} # store the new colour of the vertex
            # print("num_colour: ", num_colour)
            for vertex in graph.vertices:
                neighbour_colour = sorted([vertex.label for vertex in vertex.neighbours])
                neighbour_tuple = tuple(neighbour_colour)
                # print(colour_dict[vertex.label], neighbour_colours)
                # print("colour_dict: ", colour_dict)
                if neighbour_tuple not in colour_dict:
                    # print(neighbour_tuple, colour_dict)
                    max_colour += 1
                    colour_dict[neighbour_tuple] = max_colour
                new_dict[vertex] = colour_dict[neighbour_tuple]
            
            # update the color of the vertices    
            for vertex in graph.vertices:
                vertex.label = new_dict[vertex]
                # print("new_dict: ", new_dict)
            colour_list[index] = set([vertex.label for vertex in graph.vertices])
            # print("colour_list: ", colour_list)    
            if num_colour[index] != len(colour_list[index]):
                iteration_count[index] += 1 # update the iteration count when the color set is changed
            
        # break the loop if the color list is not changed       
        if num_colour == [len(colour) for colour in colour_list]:
            break
    # print(type(isomorphic_check(graphs, iteration_count)))
    return isomorphic_check(graphs, iteration_count)


def isomorphic_check(graphs, iteration_count):        
    isomorphic_dict = {}    
    for index, graph in enumerate(graphs[0]):  
        # print("Graph ", idx, ":", [vertex.label for vertex in graph.vertices])
        colour_set = tuple(sorted([vertex.label for vertex in graph.vertices]))
        uniqueColours = (len(colour_set) == len(set(colour_set))) # check if the color set is unique for discrete graph
    
        if colour_set not in isomorphic_dict:
            isomorphic_dict[colour_set] = tuple([[], iteration_count[index], uniqueColours])
        isomorphic_dict[colour_set][0].append(index) 
        
    res = [graph if isinstance(graph, tuple) else graph for graph in isomorphic_dict.values()]
    # print(type(res))
    print(res)
    return res

if __name__ == '__main__':
    path = "cref9vert3comp_10_27.grl"
    basic_colorref(path)          
           
                    