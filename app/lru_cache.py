import logging

logger = logging.getLogger(__name__)


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dict = {}
        logger.warning(f"LRUCache initialized with capacity {capacity}")

    def get(self, key: int) -> int:
        if key not in self._dict:
            raise KeyError
        self._dict[key] = self._dict.pop(key)
        return self._dict[key]

    def set(self, key: int, value: int) -> None:
        if key in self._dict:
            del self._dict[key]
        elif len(self._dict) == self._capacity:
            oldest_key = next(iter(self._dict.keys()))
            oldest_value = self._dict[oldest_key]
            logger.warning(f"Removing item from cache: {oldest_key} => {oldest_value}")
            del self._dict[oldest_key]
        self._dict[key] = value

    def delete(self, key: str):
        if key not in self._dict:
            raise KeyError
        return self._dict.pop(key)
