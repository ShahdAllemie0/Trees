class Node:
    
    def __init__(self, name):
        self.name = name
        self.children = []
        # self.left_child = None
        # self.right_child = None

    def add_child(self, node):
        if len(self.children) < 2:
            self.children.append(node)
            print(f"{node.name} added to the familiy!")
        else:
            print("You already got two kids. Sorry, you can't have more!")

    def remove_child(self, node):
        self.children=[child for child in self.children if child is not node]

    def traverse(self):
        nodes = [self]
        while len(nodes) != 0:
            current_node = nodes.pop()
            print(current_node.name)
            nodes += current_node.children


    def get_child_with_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

root = Node("Allemie")
full_name = input("Enter the full name (done if you're finished): ")
while full_name != "done":
    current_node = root
    names = full_name.split()[::-1]
    first_name = names.pop()
    last_name = names.pop(0)

    if current_node.name == last_name:
        if names:
            for name in names:
                child = current_node.get_child_with_name(name)
                if child:
                    current_node = child
                else:
                    new_node = Node(name)
                    current_node.add_child(new_node)
                    current_node = new_node

        current_node.add_child(Node(first_name))
        print("-"*30)
        full_name = input("Enter the full name (done if you're finished): ")




root.traverse() 
