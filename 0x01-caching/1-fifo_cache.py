#!/usr/bin/env python3
""" FifoCache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        if the number of items is higher discards first item
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                deleted_key = next(iter(self.cache_data))
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data(key)
