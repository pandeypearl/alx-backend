# 0x01. Caching

Caching algorithms including the understanding of:


   + What a caching system is
   + What FIFO means
   + What LIFO means
   + What LRU means
   + What MRU means
   + What LFU means
   + What the purpose of a caching system
   + What limits a caching system have

## Tasks

### 0. Basic dictionary
Create a class BasicCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + This caching system doesn’t have limit
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [0-basic_cache.py](0-basic_cache.py)

test file: [0-main.py](0-main.py)


### 1. FIFO caching
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
       + If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
           + you must discard the first item put in cache (FIFO algorithm)
           + you must print DISCARD: with the key discarded and following by a new line
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [1-fifo_cache.py](1-fifo_cache.py)

test file: [1-main.py](1-main.py)


### 2. LIFO Caching
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
       + If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
           + you must discard the last item put in cache (LIFO algorithm)
           + you must print DISCARD: with the key discarded and following by a new line
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [2-lifo_cache.py](2-lifo_cache.py)

test file: [2-main.py](2-main.py)


### 3. LRU Caching
Create a class LRUCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
       + If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
           + you must discard the least recently used item (LRU algorithm)
           + you must print DISCARD: with the key discarded and following by a new line
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [3-lru_cache.py](3-lru_cache.py)

test file: [3-main.py](3-main.py)


### 4. MRU Caching
Create a class MRUCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
       + If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
           + you must discard the most recently used item (MRU algorithm)
           + you must print DISCARD: with the key discarded and following by a new line
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [4-mru_cache.py](4-mru_cache.py)

test file: [4-main.py](4-main.py)


## Advanced Tasks

### 5. LFU Caching
Create a class LFUCache that inherits from BaseCaching and is a caching system:

   + You must use self.cache_data - dictionary from the parent class BaseCaching
   + You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
   + def put(self, key, item):
       + Must assign to the dictionary self.cache_data the item value for the key key.
       + If key or item is None, this method should not do anything.
       + If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
           + you must discard the least frequency used item (LFU algorithm)
           + if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
           + you must print DISCARD: with the key discarded and following by a new line
   + def get(self, key):
       + Must return the value in self.cache_data linked to key.
       + If key is None or if the key doesn’t exist in self.cache_data, return None.

file: [100-lfu_cache.py](100-lfu_cache.py)

test file: [100-main.py](100-main.py)
