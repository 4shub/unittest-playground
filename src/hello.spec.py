import unittest
import mock
from hello import *
from io import StringIO


class MyFirstTests(unittest.TestCase):
    # mock.patch() essentially allows you to modify the return value and return exceptions of existing imported
    # functions without literally editing the code of an imported function

    # in this case we are taking in builtins.open() AKA open() and making it our own via mock
    @mock.patch("builtins.open")
    def test_open_file_fail(self, mock_open):
        # side effects can be exceptions
        mock_open.side_effect = FileNotFoundError

        result = open_file('meme.txt')

        # we must tell mock that when open is called, the following arguments will be provided
        # important: always call this after you perform your test
        mock_open.assert_called_with('meme.txt', 'r')


        self.assertEqual(type(result), FileNotFoundError)


    @mock.patch("builtins.open")
    def test_open_file_success(self, mock_open):
        test_text = 'hello shello'

        # when we call open('test.text', 'r') we want to return a file that
        # StringIO emulates text returned from a file
        mock_open.return_value = StringIO(test_text)

        result = open_file('test.txt')

        # we must tell mock that when open is called, the following arguments will be provided
        # important: always call this after you perform your test
        mock_open.assert_called_with('test.txt', 'r')

        # we want to check if the file does not give us an IO error
        self.assertNotEqual(type(result), FileNotFoundError)

        # we want to check if open_file gives us the same text we saved
        self.assertEqual(result.readline(), test_text)


if __name__ == '__main__':
    unittest.main()