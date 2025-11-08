class HashTable:
    """
    Implements a Hash Table with Chaining for collision resolution
    and dynamic resizing to manage the load factor.
    """
    
    def __init__(self, initial_capacity=10):
        if initial_capacity < 1:
            raise ValueError("Initial capacity must be at least 1")
        self.capacity = initial_capacity
        self.size = 0  # Number of key-value pairs
        # Initialize the table as a list of empty lists (chains)
        self.table = [[] for _ in range(self.capacity)]
        self.resize_threshold = 0.75  # Load factor to trigger resize

    def _hash(self, key):
        """
        Private helper to compute the slot index for a given key.
        """
        # Uses Python's built-in hash() and modulo operator
        return hash(key) % self.capacity

    def _resize(self):
        """
        Private helper to resize the hash table (double capacity)
        and rehash all existing elements.
        """
        print(f"--- Resizing: Load factor exceeded {self.resize_threshold} ---")
        print(f"Old capacity: {self.capacity}, New capacity: {self.capacity * 2}")
        
        old_table = self.table
        new_capacity = self.capacity * 2
        
        # Reset the table with new capacity
        self.capacity = new_capacity
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0  # Size will be reset by re-inserting
        
        # Rehash all items from the old table into the new one
        for chain in old_table:
            for key, value in chain:
                self.insert(key, value) # insert() handles size increment

    def insert(self, key, value):
        """
        Adds a key-value pair to the hash table.
        If the key already exists, its value is updated.
        """
        # 1. Check if resizing is needed BEFORE insertion
        load_factor = (self.size + 1) / self.capacity
        if load_factor > self.resize_threshold:
            self._resize()
            
        # 2. Find the chain for the key
        index = self._hash(key)
        chain = self.table[index]
        
        # 3. Check if key already exists in the chain
        for i, (existing_key, existing_value) in enumerate(chain):
            if existing_key == key:
                # Key found, update value and return
                chain[i] = (key, value)
                return
                
        # 4. Key not found, append new (key, value) pair
        chain.append((key, value))
        self.size += 1

    def search(self, key):
        """
        Retrieves a value associated with a given key.
        Raises KeyError if the key is not found.
        """
        # 1. Find the chain
        index = self._hash(key)
        chain = self.table[index]
        
        # 2. Search the chain for the key
        for existing_key, value in chain:
            if existing_key == key:
                return value
                
        # 3. Key not found
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        """
        Removes a key-value pair from the hash table.
        Raises KeyError if the key is not found.
        """
        # 1. Find the chain
        index = self._hash(key)
        chain = self.table[index]
        
        # 2. Search the chain for the key
        for i, (existing_key, value) in enumerate(chain):
            if existing_key == key:
                # Key found, remove the (key, value) tuple
                chain.pop(i)
                self.size -= 1
                return
                
        # 3. Key not found
        raise KeyError(f"Key not found: {key}")

    def __len__(self):
        """Returns the number of items (key-value pairs) in the table."""
        return self.size

    def __str__(self):
        """Returns a string representation of the hash table."""
        lines = []
        for i, chain in enumerate(self.table):
            if chain: # Only print non-empty slots
                lines.append(f"Slot {i}: {chain}")
        return "\n".join(lines)


if __name__ == "__main__":
    print("--- Initializing Hash Table (Capacity=5) ---")
    ht = HashTable(initial_capacity=5)
    
    print("\n--- Inserting items ---")
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    print(ht)
    print(f"Current Size: {len(ht)}, Capacity: {ht.capacity}")

    print("\n--- Inserting item to trigger resize ---")
    # (3+1) / 5 = 0.8, which is > 0.75
    ht.insert("grape", 4) 
    print(ht)
    print(f"Current Size: {len(ht)}, Capacity: {ht.capacity}")

    print("\n--- Inserting more items ---")
    ht.insert("mango", 5)
    ht.insert("papaya", 6)
    ht.insert("kiwi", 7)
    
    print("\n--- Inserting item to trigger second resize ---")
    # (7+1) / 10 = 0.8, which is > 0.75
    ht.insert("lemon", 8)
    print(ht)
    print(f"Current Size: {len(ht)}, Capacity: {ht.capacity}")

    print("\n--- Searching for items ---")
    try:
        print(f"Search 'banana': {ht.search('banana')}")
        print(f"Search 'kiwi': {ht.search('kiwi')}")
        print(f"Search 'apple': {ht.search('apple')}")
    except KeyError as e:
        print(e)

    print("\n--- Deleting an item ---")
    try:
        print("Deleting 'orange'...")
        ht.delete("orange")
        print(f"Search 'orange': {ht.search('orange')}")
    except KeyError as e:
        print(e)
        
    print("\n--- Final Table State ---")
    print(ht)
    print(f"Final Size: {len(ht)}, Final Capacity: {ht.capacity}")
    
    print("\n--- Searching for non-existent item ---")
    try:
        print(f"Search 'grapefruit': {ht.search('grapefruit')}")
    except KeyError as e:
        print(e)
