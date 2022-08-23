from collections import deque;


def search_fast(graph, cost , parents):
    queue = deque()
    queue += graph['start'].keys()
    while queue:
        node = queue.popleft() 

        

    return False




if __name__ == '__main__':

    infinite = float('inf')
    way = {}

    # way["start"]= ["a","b"]
    # way["start"]["a"] = 6
    # way["start"]["b"] = 6
    # way["a"] = ["end"]
    # way["a"]["end"] = 1
    # way["b"]= ["a","end"]
    # way["b"]["a"] = 6
    # way["b"]["end"] = 5
    # way["end"]= []

    way['start'] = {
        'a' : 6,
        'b' : 2
    }

    way['a'] = {
        'end' : 1,
    }
    way['b'] = {
        'a' : 3,
        'end' : 5,
    }
    cost = {}

    cost['a']=6
    cost['b']=2
    cost['end']= infinite

    parents = {}

    parents['a']= "start"
    parents['b']= "start"
    parents['end']= None
    
    search_fast(way, cost, parents)

    




    