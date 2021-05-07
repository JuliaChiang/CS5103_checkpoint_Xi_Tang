import unittest
import word_count
import config
from unittest.mock import patch
test_str = config.test_string



class TestWordMethods(unittest.TestCase):

    def test_count_no_word(self):
        self.count = word_count.word_count("")
        self.assertEqual(self.count, 0)

    def test_count_tab(self):
        self.count = word_count.word_count("\t")
        self.assertEqual(self.count, 0)

    def test_count_new_line(self):
        self.count = word_count.word_count("\n")
        self.assertEqual(self.count, 0)

    def test_count_period(self):
        self.count = word_count.word_count(".")
        self.assertEqual(self.count, 0)

    def test_count_one_word(self):
        self.count = word_count.word_count("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(self.count, 1)

    def test_count_one_word_with_two_seperators(self):
        self.count = word_count.word_count("\nabcdefghijklmnopqrstuvwxyz\t")
        self.assertEqual(self.count, 1)

    def test_count_one_word_with_sperator_at_the_end(self):
        self.count = word_count.word_count("abcdefghijklmnopqrstuvwxyz\t")
        self.assertEqual(self.count, 1)

    def test_count_one_word_with_sperator_at_the_start(self):
        self.count = word_count.word_count("?abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(self.count, 1)

    def test_count_two_words_with_space(self):
        self.count = word_count.word_count("abcdefghijklm nopqrstuvwxyz")
        self.assertEqual(self.count, 2)

    def test_count_multiple_words_with_space(self):
        self.count = word_count.word_count("ab cd ef\t gh \n mn, ls. ty? we; ok")
        self.assertEqual(self.count, 9)

    def test_count_duplicates(self):
        self.count = word_count.word_count("abc abc")
        self.assertEqual(self.count, 1)

class TestCharMethods(unittest.TestCase):
    def test_count_no_char(self):
        self.count = word_count.char_count("")
        self.assertEqual(self.count, 0)

    def test_count_seperator_char(self):
        self.count = word_count.char_count("\n")
        self.assertEqual(self.count, 0)

    def test_count_chars(self):
        self.count = word_count.char_count("abcde\n")
        self.assertEqual(self.count, 5)


class TestLineMethods(unittest.TestCase):
    def test_count_one_line(self):
        self.count = word_count.line_count("abcde")
        self.assertEqual(self.count, 1)

    def test_count_one_line_with_seperator(self):
        self.count = word_count.line_count("abcde\n")
        self.assertEqual(self.count, 2)

    def test_count_new_line(self):
        self.count = word_count.line_count("\n")
        self.assertEqual(self.count, 2)

    def test_count_lines(self):
        self.count = word_count.line_count("abcde\nfgh\n")
        self.assertEqual(self.count, 3)

class TestReplaceMethods(unittest.TestCase):
    @patch('builtins.input', side_effect = ['a', 'xh'])
    def test_replace_not_word(self, mock_input):
        self.text = word_count.word_replace(test_str)
        self.assertEqual(self.text, "ab cd ef")

    @patch('builtins.input', side_effect = ['ab', 'xh'])
    def test_replace_one_word(self, mock_input):
        self.text = word_count.word_replace(test_str)
        self.assertEqual(self.text, "xh cd ef")

    @patch('builtins.input', side_effect = ['ab', 'xh'])
    def test_replace_two_words(self, mock_input):
        mock_input.side_effect = ['ab', 'xh']
        self.text = word_count.word_replace("ab cd ab")
        self.assertEqual(self.text, "xh cd xh")

if __name__ == '__main__':
    unittest.main()