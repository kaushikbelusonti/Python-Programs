# Problem
'''
Question: Maximum XOR of String Lengths Across Connected Groups

You are given:

    A list of strings words where nn is the total number of strings.
    A list of pairs pairs, where each pair [i, j] represents that the strings at indices i and j are connected. Strings are indirectly connected if there is a path between them through other pairs.

Tasks:

    Identify all groups of connected strings based on the pairs list.
    For each group, calculate the maximum XOR of the lengths of the strings within that group.
    Return the largest XOR value among all groups. If no groups exist, return 0.

Example:
Input:

words = ["abc", "def", "gh", "ijk", "lm"]
pairs = [[0, 1], [1, 2], [3, 4]]

Output:

1

Explanation:

    Groups of connected strings:
        Group 1: Indices [0, 1, 2] → Strings ["abc", "def", "gh"] → Lengths [3, 3, 2].
        Group 2: Indices [3, 4] → Strings ["ijk", "lm"] → Lengths [3, 2].

    Maximum XOR of lengths for each group:
        Group 1: 3⊕3=03⊕3=0, 3⊕2=13⊕2=1, 2⊕3=12⊕3=1. Maximum = 11.
        Group 2: 3⊕2=13⊕2=1. Maximum = 11.

    Largest XOR value among all groups = 1.
'''
### Inputs
words = ["abc", "def", "gh", "ijk", "lm"]
pairs = [[0, 1], [1, 2], [3, 4]]

### Code starts from here

# Calculate the sum of the elements in the list in pairs
p = [] # Initialize an empty list to store the sum of elements in internal list
for element in pairs:
    p.append(sum(element))    
p = sorted(p)
#print(f"List with sum of elements in pair: {p}")

# Extract the connected strings
i = 0
connected_pairlist = []
while i < len(p):
    conn_pair = [p[i]//2, p[i]//2 + 1]
    i += 1
    j = i 
    while j < len(p):
        if p[j] - p[j-1] == 2:
            conn_pair.append((p[j]//2)+1)
            j += 1
            i = j 
        else:
            j = len(p)
    connected_pairlist.append(conn_pair)
    
#print(f"Connected pair list: {connected_pairlist}")

# Calculate the word length of the connected pair list
word_length = []
for i, word in enumerate(words):
    word_length.append(len(word))
    
connected_word_length = []

for i, element in enumerate(connected_pairlist):
    conn_pair = []
    n = len(element)
    k = 0
    while k < n:
        conn_pair.append(word_length[element.pop(0)])
        k += 1
    connected_word_length.append(conn_pair)
        
#print(f"Connected word length: {connected_word_length}")

# Find maximum XOR

max_xor = 0

for a in connected_word_length:
    xor = 0
    for b in a:
        xor ^= b 
    if xor > max_xor:
        max_xor = xor
        
print(f"Maximum Exclusive-OR of connected string lengths: {max_xor}")