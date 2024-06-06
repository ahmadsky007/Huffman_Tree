import heapq


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


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
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None


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


# Example usage:
data = "aaaaab"
tree = build_huffman_tree(data)
codebook = generate_huffman_codes(tree)
encoded_data = encode(data, codebook)
decoded_data = decode(encoded_data, tree)

print("Original:", data)
print("Encoded:", encoded_data)
print("Decoded:", decoded_data)
