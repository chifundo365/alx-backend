#!/usr/bin/env python3
"""
Implements a Basic caching System
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Cashing system """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
        add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
