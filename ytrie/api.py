'''
API module
'''


class ytrie(object):
    '''
    API to access trie data.
    '''

    def __init__(self, trie_list=None, end_key='__end__', end_value=None):
        if not trie_list:
            trie_list = []
        self.__trie = {}
        self.__endkey = end_key
        self.__endvalue = end_value
        self.append(trie_list)

    @property
    def end_key(self):
        return self.__endkey

    @end_key.setter
    def end_key(self, key):
        assert key is not None, 'end_key cannot be set to None'
        if key != self.__endkey:
            self.__setend(key=key)
            self.__endkey = key

    @property
    def end_value(self):
        return self.__endvalue

    @end_value.setter
    def end_value(self, value):
        if value != self.__endvalue:
            self.__setend(value=value)
            self.__endvalue = value

    def __setend(self, key=None, value=None):
        key_list = list(self.__getitem__(''))
        for child in key_list:
            data = self.__trie
            for letter in child:
                data = data[letter]
            if key is not None:
                data[key] = data.pop(self.__endkey)
            if value is not None:
                data[self.__endkey] = value

    def __getitem__(self, item):
        data = self.__trie
        for letter in item:
            data = data[letter]
        for child in self.__getitem(data):
            yield item + ''.join(child)

    def __getitem(self, data):
        for k, v in data.items():
            if k == self.__endkey:
                yield []
            else:
                for key in self.__getitem(data[k]):
                    yield [k] + key

    def append(self, trie_list):
        for item in trie_list:
            self.__additem(item)

    def __additem(self, item):
        data = self.__trie
        try:
            for index, letter in enumerate(item):
                data = data[letter]
        except KeyError:
            leftover_items = item[index:]
        else:
            leftover_items = []
        for letter in leftover_items:
            data[letter] = {}
            data = data[letter]
        data[self.__endkey] = self.__endvalue

    def __add__(self, item):
        assert isinstance(item, ytrie), 'Can only add ytrie objects'
        assert self.end_key == item.end_key, 'Can only add ytrie ' + \
                                             'objects with same end_key'
        assert self.end_value == item.end_value, 'Can only add ytrie ' + \
                                                 'objects with same end_value'
        return_trie = ytrie()
        trie_list = list(self.__getitem__('')) + list(item[''])
        return_trie.append(trie_list)
        return return_trie
