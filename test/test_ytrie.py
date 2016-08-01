"""
Tests for `ytrie` module.
"""
import pytest
from ytrie import ytrie


@pytest.fixture
def starting_dict():
    # my_trie = {
    #           'G': {
    #                'O': {
    #                     '__end__': None,
    #                     'A': {
    #                          'T': {
    #                               '__end__': None
    #                               }
    #                          },
    #                     'N': {
    #                          'E': {
    #                               '__end__': None
    #                               }
    #                          }
    #                     }
    #                }
    #           }
    return {'GO', 'GOAT', 'GONE'}


def test_init_with_defaults():
    my_trie = ytrie()
    assert my_trie._ytrie__trie == {}
    assert my_trie._ytrie__endkey == '__end__'
    assert my_trie._ytrie__endvalue is None


def test_init_with_trie_dict():
    trie_dict = {"a": {"b": {"__end__": None}}}
    my_trie = ytrie(trie_list=['ab'])
    assert my_trie._ytrie__trie == trie_dict


def test_init_with_end_key():
    my_trie = ytrie(end_key='__myend__')
    assert my_trie._ytrie__endkey == '__myend__'


def test_init_with_end_value():
    my_trie = ytrie(end_value='__myend__')
    assert my_trie._ytrie__endvalue == '__myend__'


@pytest.mark.parametrize("query, expected", [
    ("", {'GO', 'GOAT', 'GONE'}),
    ("GO", {'GO', 'GOAT', 'GONE'}),
    ("GOA", {'GOAT'}),
])
def test_get_all_items(starting_dict, query, expected):
    my_trie = ytrie(trie_list=starting_dict)
    assert set(my_trie[query]) == expected


def test_add_items():
    my_trie = ytrie()
    add_set = {'TEST', 'TENT', 'TENNIS', 'TEA', 'TRY'}
    my_trie.append(add_set)
    assert set(my_trie['']) == add_set


def test_add_two_my_tries(starting_dict):
    my_trie1 = ytrie(starting_dict)
    my_trie1_set = {'GO', 'GOAT', 'GONE'}
    my_trie2 = ytrie()
    my_trie2_set = {'TEST', 'TENT', 'TENNIS', 'TEA', 'TRY'}
    my_trie2.append(my_trie2_set)
    my_trie = my_trie1 + my_trie2
    assert set(my_trie['G']) == my_trie1_set
    assert set(my_trie['T']) == my_trie2_set


def test_set_end_key(starting_dict):
    my_trie1 = ytrie(starting_dict)
    my_trie1.end_key = '__myend__'
    assert my_trie1._ytrie__trie['G']['O']['__myend__'] is None
    assert my_trie1.end_key == '__myend__'


def test_set_end_value(starting_dict):
    my_trie1 = ytrie(starting_dict)
    my_trie1.end_value = '__myend__'
    assert my_trie1._ytrie__trie['G']['O']['__end__'] == '__myend__'
    assert my_trie1.end_value == '__myend__'


@pytest.mark.parametrize("end_key, end_value, exception", [
    ('__myend__', None, 'Can only add ytrie objects with same end_key'),
    ('__end__', '__myend__', 'Can only add ytrie objects with same end_value')
])
def test_add_different_ytries(starting_dict, end_key, end_value, exception):
    my_trie1 = ytrie(starting_dict)
    my_trie1.end_key = end_key
    my_trie1.end_value = end_value
    my_trie2 = ytrie({'I': {'__end__': None}})
    with pytest.raises(AssertionError) as excinfo:
        my_trie = my_trie1 + my_trie2
    assert exception in str(excinfo.value)


def test_change_both_end_key_cannot_be_none(starting_dict):
    my_trie1 = ytrie(starting_dict)
    with pytest.raises(AssertionError) as excinfo:
        my_trie1.end_key = None
    assert 'end_key cannot be set to None' in str(excinfo.value)
