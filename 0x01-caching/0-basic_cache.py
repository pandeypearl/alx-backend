#!/usr/bin/env python3
""" Basic Cache Dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching """

    def put(self, key, item):
        """ Assigns to dictionary self.cache_data
        the item value for the key key """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return value in
        self.cache_data linked to key """
        return self.cache_data.get(key, None)
