class Node:
    def __init__(self, value, treeno):
        self.val = value
        self.sons = {}
        self.source = {treeno}

    def show(self, level=0):
        print('\t' * level + repr(self.val))
        for child in self.sons:
            self.sons[child].show(level+1)


class SuffixTree:
    def __init__(self):
        self.root = Node('root', None)

    def insert(self, suffix, treeno):
        head = self.root

        i = 0
        while suffix[i] in head.sons:
            head = head.sons[suffix[i]]
            head.source.add(treeno)
            if i < len(suffix)-1:
                i += 1
            else:
                break

        for item in suffix[i:]:
            head.sons[item] = Node(item, treeno)
            head = head.sons[item]
        
        head.sons['$'] = Node('$', treeno)
        head.source.add(treeno)

    def search(self, pattern):
        head = self.root
        source = set()

        i = 0
        while pattern[i] in head.sons:
            head = head.sons[pattern[i]]
            if source == set():
                source.union(head.source) 
            else:
                source.intersection_update(head)

            if i < len(pattern)-1:
                i += 1
            else:
                break
        
        if i == len(pattern)-1:
            res = list(head.source)
            res.sort()
            print('find in', *res)
        else:
            print('not find')


