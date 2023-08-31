"""
Section 3: Theory Qs

3.1
Design a basic hash function, keeping in mind memory constraints
and how you would deal with hash collisions.
"""


class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.table = [None] * table_size

    def hash_function(self, key):
        return key % len(self.table)

    def insert(self, key, value):
        hash_index = self.hash_function(key)
        # If the slot is already occupied look for an empty slot and update the key
        while self.table[hash_index] is not None:
            # If the key exists, update its value
            if self.table[hash_index][0] == key:
                self.table[hash_index][1] = value
                return
            # If the key does not exist give it a new hash index
            hash_index = (hash_index + 1) % len(self.table)
        self.table[hash_index] = [key, value]

"""
Memory constraints have to do with the size of the table. 
The smaller the table the less memory is needed but more collisions may occur.
To deal with these collisions the key must be updated by giving it a new index.
"""


