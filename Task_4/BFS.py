from collections import deque  # deque is an efficient queue

def BFS(graph, start, goal):
    visited = {start} # We use a set because we only need to check for membership. A set is best for this

    # Frontier: [(node, [path])]
    frontier = deque([(start, [start])])  # Here we store the node, and the path we took to get to that node

    while frontier: # We repeat until the frontier is empty, this means we have exhausted all the nodes
        current, path = frontier.popleft() 
        
        if current == goal:
            return path # We return the path it took us to get to the node

        for neighbor in graph[current]: # Here, graph is represented using an adjacency list, thus {node: [neighbours]}
            if neighbor not in visited: # We check if we have already seen the node to prevent duplication and cycles
                visited.add(neighbor)   # Add the neighbour to the visited set to ensure we don't add it to the frontier again if we meet it
                frontier.append((neighbor, path + [neighbor])) # Add the node to the frontier, we do path + [neigbour] instead of appending, to ensure that we create a new list
    
    # If we complete the frontier without reaching the goal, then there is not path
    return "No path found" 

def main():
    # We're representing the graph using an adjacency list
    myGraph = {
        'A': ['C', 'D', 'E'],
        'B': ['F'],
        'C': ['B', 'F'],
        'D': [],
        'E': ['C'],
        'F': ['G'],
        'G': ['C']
    }


    start_node = 'A'
    goal_node  = 'G'
    
    result = BFS(myGraph, start_node, goal_node)
    print(result)


if __name__ == "__main__":        
    main()