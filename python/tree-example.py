from bintrees import AVLTree

tree = AVLTree([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j')])
tree.insert(11, 'k')
tree.remove(5)
print(tree)
print(tree.get(4))

for i in tree:
    print(i)


