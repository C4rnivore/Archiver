class Node():
    freq = 0

    def __init__(self, left_node,  right_node, left_node_freq = None, right_node_freq  = None):
        if isinstance(left_node, Node):
            self.freq += left_node.freq

        if isinstance(right_node, Node):
            self.freq += right_node.freq

        if isinstance(left_node, str):
            self.freq += left_node_freq
            
        if isinstance(right_node, str):
            self.freq += right_node_freq
        else:
            Exception('Nodes must be neither Node-class or str')

        self.left_node = left_node
        self.right_node = right_node
