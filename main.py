class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item):
        self.elements.append(item)
        self.elements.sort(key=lambda x: x.freq)

    def get(self):
        return self.elements.pop(0)


def calculate_frequencies(data):
    frequencies = {}
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def build_huffman_tree(data):
    frequencies = calculate_frequencies(data)
    priority_queue = PriorityQueue()

    for char, freq in frequencies.items():
        priority_queue.put(HuffmanNode(char, freq))

    while len(priority_queue.elements) > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        priority_queue.put(merged)

    return priority_queue.get() if not priority_queue.is_empty() else None


def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook


def encode(data, codebook):
    return ''.join(codebook[char] for char in data)


def decode(encoded_data, tree):
    decoded_output = []
    current_node = tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = tree
    return ''.join(decoded_output)


# Example usage
data = "AHMAD"
tree = build_huffman_tree(data)
codebook = generate_huffman_codes(tree)
encoded_data = encode(data, codebook)
decoded_data = decode(encoded_data, tree)

print("Codebook:", codebook)
print("Original:", data)
print("Encoded:", encoded_data)
print("Decoded:", decoded_data)
