========
Usage
========

To use ytrie in a project::

	>>> import ytrie
	>>> my_trie = ytrie()
	>>> mytrie.append(['TEST', 'TENT', 'TENNIS', 'TEA', 'TRY'])
	>>> list(mytrie[''])
	['TEST', 'TENT', 'TENNIS', 'TEA', 'TRY']
	>>> list(mytrie['TEN'])
	['TENT', 'TENNIS']
