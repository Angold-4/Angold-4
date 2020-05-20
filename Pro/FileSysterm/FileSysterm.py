# Wange 20200518
import os
from matplotlib import pyplot as plt


class File:
    """A File Systerm"""

    def __init__(self, filename, path=''):
        """Make The Path And Check Whether It Is a Correct Path"""

        Path = os.path.join(path, filename)
        self._path = Path
        self._name = filename

        try:
            _tfile = open(self._path)
        except IOError as e:
            raise IOError("can't open the file or file not found", e)
        else:
            _tfile.close()

    def get_filename(self):
        return self._name

    def get_filepath(self):
        return self._path

    def get_content(self):
        """Return The Hole Content"""
        _file = open(self._path)
        return _file.read()

    def get_lines(self):
        """Return The Number of File"""
        _c = 0
        _file = open(self._path)
        for i in _file:
            _c += 1
        _file.close()
        return _c

    def count_letter(self, letter):
        """Count the Appearance Times of Given Letter in A File"""
        _c = 0
        _file = open(self._path)
        for i in _file.read():
            if i == letter:
                _c += 1
        _file.close()
        return _c

    def count_word(self, word):
        """Count the Appearance Times of Given Word in A File"""
        _dict = self.count_words()
        if word in _dict:
            return _dict[word]
        else:
            return ("file don't included that word")

    def count_letters(self, Table=False):
        """Count the Appearance times of All Str in A File

        Choose the Table If You Want to Display As a Bar Graph
        """
        _list = []
        _file = open(self._path)
        for i in _file.read():
            if i not in _list:
                _list.append(i)

        _dict = dict.fromkeys(_list, 0)
        _file = open(self._path)
        for i in _file.read():
            _dict[i] += 1
        try:
            del _dict[' ']
        except KeyError:
            pass
        if Table:
            xs = list(_dict.keys())
            ys = list(_dict.values())
            plt.bar(xs, ys)
            plt.show()
        return _dict

    def count_words(self, Table=False):
        """Count the Appearance times of All Words in A File

        Choose the Table If You Want to Display As a Bar Graph
        """
        _wordlist = []
        _symbol = (',', '.', ';', ':', '*', '+', '-', '=', ' ', '(', ')',
                   '\'', '\"', '\n', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1',
                   '2', '3', '4', '5', '6', '7', '8', '9', '0', '#', '!',
                   '<', '>', '/', '[', ']', '{', '}', '?', '%', '$')
        _file = open(self._path)
        _wordlists = []
        for i in _file.read():
            if i in _symbol:
                _word = ''.join(_wordlist)
                _wordlists.append(_word)
                _wordlist = []
            else:
                _wordlist.append(i)
        _dict = dict.fromkeys(_wordlists, 0)

        _file = open(self._path)
        for i in _file.read():
            if i in _symbol:
                _word = ''.join(_wordlist)
                _dict[_word] += 1
                _wordlist = []
            else:
                _wordlist.append(i)
        try:
            del _dict['']
        except KeyError:
            pass
        if Table:
            xs = list(_dict.keys())
            ys = list(_dict.values())
            plt.bar(xs, ys)
            plt.show()
        return _dict
