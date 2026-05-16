from collections import deque # Deque is better than a normal list for a queue

def DFS(graph, start, goal):
    visited = set() # we're just checking for membership, thus a set is optimal

    def helper(graph, current): # Here we're using a helper function so that we don't have to explicitly pass the visited set each time. 
        visited.add(current) # We add the node  to the visited set to avoid repeating it
        if current == goal: # If we found our goal, we immediately return
            return deque([current]) 
        
        for neigbour in graph[current]: # Here we loop through all the neigbours of our current node
            if neigbour not in visited: # Verify we haven't visited it before
                r = helper(graph, neigbour) # Used this to store our return value, to know whether we returned early or not
                if r: # If we returned early due to finding the goal, we stop recursing and start unwinding 
                    r.appendleft(current) # We're rebuilding the path, we attach the current node to the path before returning
                    return r #Return the built path to the parent function
    
    path = helper(graph, start) # Calling our helper function
    if path: # If we found a path we return it
        return path
    else:# If not path was found, path will be void
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
    
    result = DFS(myGraph, start_node, goal_node)
    print(result)


if __name__ == "__main__":        
    main()