#!/usr/bin/env python3
""" LifoCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        if the number of items is higher discards last item
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                deleted_key = list(iter(self.cache_data))[-1]
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
