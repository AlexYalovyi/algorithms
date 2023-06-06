from collections import deque

def is_seller(name):
    return name[-1] == 'm'

def search(graph, name):
    search_queue = deque()
    searched = set()
    search_queue += [[name]]

    while len(search_queue) > 0:
        line = search_queue.popleft()
        person = line[-1]

        if person in searched:
            continue
        else:
            searched.add(person)
            if is_seller(person):
                return line
            else:
                search_queue.extend(list(map(lambda x: line + [x],graph[person])))
    
    return False



graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(search(graph, "you"))