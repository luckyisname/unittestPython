import unittest

from name import get_formatted_name

class FirstTestCase(unittest.TestCase):
    '''Tests running'''

    def test_first_last_name(self):
        '''Names with two words right working'''
        formatted_name = get_fotmatted_name('bob', 'dylan')
        self.assertEqual(formatted_name, 'Bob Dylan')

    if __name__ == '__main__':
        unittest.main()
