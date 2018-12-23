import sys
import functools
from collections import OrderedDict

with open(sys.argv[1], 'r') as f:
    data = f.read().split('\n')
    rules = [[rule.split()[1], rule.split()[7]] for rule in data[0: -1]]

node_set = sorted(functools.reduce(lambda a,c : set(a).union(set(c)), rules))

nodes = OrderedDict()
order = []

for node in node_set:
  requirements = [rule[0] for rule in rules if rule[1] == node]
  nodes[node] = {
    'complete': False,
    'req': requirements,
  }

while(len(node_set) != len(order)):
    for label, node in nodes.items():
        req = node['req']
        if node['complete']: continue
        if not req or not [False for r in req if not nodes[r]['complete']]:
            nodes[label]['complete'] = True
            order.append(label)
            break
    
print(''.join(order))
    
