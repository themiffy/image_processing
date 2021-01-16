queryQuantity = int(input())
namespaces = {'global': {'parent': 'None', 'vars':set()}} # ключ - namespace. значение - parent3

def create(namespace,parent):
    namespaces[namespace] = {'parent':parent, 'vars':set()}

def add(namespace,var):
    namespaces[namespace]['vars'].add(var)

def get(namespace,var):
    if namespace == 'None':
        return 'None'
    if var in namespaces[namespace]['vars']:
        return namespace
    return get(namespaces[namespace]['parent'],var)

for i in range(queryQuantity):
    cmd, namesp, arg = input().split() 
    if cmd == 'create':
        create(namesp,arg)
    
    if cmd == 'add':
        add(namesp,arg)

    if cmd == 'get':
        print(get(namesp,arg))