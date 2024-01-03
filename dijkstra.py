from PriorityQueue import PriorityQueue



def dijkstra(graph, start):
    previous = {v: None for v in graph.adjacency_list.keys()}
    visited = {v: False for v in graph.adjacency_list.keys()}
    distances = {v: float("inf") for v in graph.adjacency_list.keys()}

    distances[start] = 0
    pq = PriorityQueue()

    pq.add_task(0, start)

    while pq:
        removed_distance, removed = pq.pop_task()
        visited[removed] = True

        for edge in graph.adjacency_list[removed]:
            if visited[edge.node]:
                continue

            new_distance = removed_distance + edge.distance

            if new_distance < distances[edge.node]:
                distances[edge.node] = new_distance
                previous[edge.node] = removed
                pq.add_task(new_distance, edge.node)

    previous_str = {str(k): str(v) for k, v in previous.items()}
    visited_str = {str(k): v for k, v in visited.items()}
    distances_str = {str(k): v for k, v in distances.items()}


    print("Previous:", previous_str)
    print("Visited:", visited_str)
    print("Distances:", distances_str)

    return




