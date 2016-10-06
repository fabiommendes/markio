import pytest
from markio.data_structures import ParentDict


def test_parent_dict():
    parent = {'baz': 'spam'}
    d = ParentDict(parent, foo='bar')
    assert 'baz' in d
    assert len(d) == 2
    assert set(d) == {'baz', 'foo'}
