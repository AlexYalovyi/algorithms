import random

def search(graph):
    need_to_visit = list(graph.keys())
    current_city = random.choice(need_to_visit)
    need_to_visit.remove(current_city)
    path = [current_city]
    print('init city', current_city)

    while len(need_to_visit) > 0:
        neighbours = list(graph[current_city].keys())
        closest_city = need_to_visit[0]
        closest_distance = graph[current_city][closest_city]


        for neighbour in neighbours:
            if graph[current_city][neighbour] < closest_distance and neighbour in need_to_visit:
                closest_city = neighbour
        
        path.extend([closest_city])
        need_to_visit.remove(closest_city)
        current_city = closest_city

    return path


graph = {}
graph['marin'] = { 'san_francisko': 2, 'berkley': 1, 'fremont': 4 }
graph['san_francisko'] = { 'marin': 1.5, 'berkley': 1.5, 'fremont': 3 }
graph['berkley'] = { 'san_francisko': 1.5, 'marin': 1.5, 'fremont': 1 }
graph['fremont'] = { 'san_francisko': 4, 'berkley': 1, 'marin': 4 }


print('closest path is', search(graph))
