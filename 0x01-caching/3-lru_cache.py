#!/usr/bin/env python3
""" Implements LRUCache """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """Add an item in the cache
        if the number of items is higher:
            discards the least recently used item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_keys:
                self.used_keys.append(key)
            else:
                self.used_keys.append(
                        self.used_keys.pop(self.used_keys.index(key)))
            if len(self.used_keys) > BaseCaching.MAX_ITEMS:
                discard = self.used_keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))

    def get(self, key):
        """ Get an item by key """
        if self.cache_data.get(key):
            self.used_keys.append(
                    self.used_keys.pop(self.used_keys.index(key)))
        return self.cache_data.get(key)
