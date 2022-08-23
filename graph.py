from collections import deque;





def search_seller(graph):
    queue = deque()
    queue += graph['Valen']
    while queue:
        name = queue.popleft()
        if (is_end(name)):
            print(name, 'is mango seller')
            return True
        else:
            queue += graph[name]
    return False
def search_shortest(graph):
    queue = deque()
    queue += graph['start']
    while queue:
        print(queue)
        name = queue.popleft()
        if (is_end(name)):
            print('end')
            
            return True
        else:
            queue += graph[name]
    return False
def multiplication_table(number):
    for i in number:
        print(i * number)



def is_mango_seller(name):
    return name[-1] == 'm'
def is_end(name):
    return name == 'end'


if __name__ == "__main__":
    graph = {}
    # graph['Valen'] = ['bob','alice','claire']
    # graph['bob'] = ['anuj','peggy']
    # graph['alice'] = ['peggy']
    # graph['claire'] = ['thom','jonny']
    # graph['anuj'] = []
    # graph['thom'] = []
    # graph['jonny'] = []
    # graph['peggy'] = []



    graph["start"]= {
        'a': 1 ,
        'b' : 1
        }
    graph["a"]= {
        'd' : 1
    }
    graph["b"]= {
        'c': 1,
        'a': 1,
        'e': 1
    }
    graph["c"]= {
        'd' : 1
    }
    graph["d"]= {
        'g' : 1
    }
    graph["e"]= {
        'g': 1,
        'f': 1,
    }
    graph["f"]= {
        'g' : 1
    }
    graph["g"]= {
        'end' : 1
    }


    graph["end"]= {}
    # graph["a"] = ["end"]
    # graph["b"]= ["a","end"]
    # way["a"]["end"] = 1
    # way["b"]["a"] = 6
    # way["b"]["end"] = 5
    # multiplication_table(10)
    print(matrix)
    search_shortest(graph)

