import os
import unittest

def analyse_text(filename):
    '''Determine the number of lines and characters in the file.
    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or cannot be read.

    Returns: A tuple containing number of lines and characters in the file
    
    '''
    nb_line = 0
    nb_character = 0

    with open(filename, 'r') as f:
        for line in f:
            nb_line += 1
            nb_character += len(line)

    return (nb_line, nb_character)


class TextAnalysisTests(unittest.TestCase):
    '''Test for analyse_text() function'''

    def setUp(self):
        '''This function is run before all the test cases
        It will create a file for the text methods to use.
        '''
        self.filename = 'file_to_analyse.txt'
        with open(self.filename, 'w') as f:
            f.write('This is my new file to test.\n'
                    'It does not contain much more information.\n'
                    'But it will be helpful for understanding the unittest.')
    

    def tearDown(self):
        '''This function will be executed after all the test cases.
        It will delete the file used by the test methods.
        '''
        try:
            os.remove(self.filename)
        except:
            pass


    def test_function_runs(self):
        '''Basic smoke test: does the function run.'''
        analyse_text(self.filename)

    
    def test_line_count(self):
        '''Checks that the line count is correct.'''
        self.assertEqual(analyse_text(self.filename)[0], 3)


    def test_charecter_count(self):
        '''Checks that the character count is correct.'''
        self.assertEqual(analyse_text(self.filename)[1], 126)


    def test_no_such_file_name(self):
        '''Checks that the proper exception is thrown for a missing file'''
        with self.assertRaises(IOError):
            analyse_text("no_such_file.txt")


    def test_no_deletion(self):
        '''Checks that the function does not delete the given file'''
        analyse_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()