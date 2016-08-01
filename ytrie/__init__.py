'''
ytrie library
~~~~~~~~~~~~~~~~~~~~~
ytrie is a library, written in Python, to provide APIs access to trie data.
   >>> import ytrie
   >>> my_trie = ytrie()
   >>> mytrie.append(['TEST', 'TENT', 'TENNIS', 'TEA', 'TRY'])
   >>> list(mytrie[''])
   ['TEST', 'TENT', 'TENNIS', 'TEA', 'TRY']
   >>> list(mytrie['TEN'])
   ['TENT', 'TENNIS']
'''

from .api import ytrie

__author__ = 'Ashwin Venkatesan'
__email__ = 'ashwinjv@gmail.com'
__version__ = '0.1.0'
