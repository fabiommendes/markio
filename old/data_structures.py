#
# We may need this later
#
import collections


class ParentDict(collections.MutableMapping):
    """
    A dictionary that can look for data in a parent mapping.
    """

    def __init__(self, parent, *args, **kwds):
        self._data = dict(*args, **kwds)
        self._parent = parent

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self._parent[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        try:
            del self._data[key]
        except KeyError:
            if key not in self._parent:
                raise

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        used = set()
        for k in self._data:
            used.add(k)
            yield k
        for k in self._parent:
            if k not in used:
                used.add(k)
                yield k

    def __str__(self):
        return str(dict(self))

    def owned(self):
        """
        Return a dictionary with a copy of all data that is owned by the
        default dict.
        """

        return dict(self._data)
