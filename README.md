# python-unittest  
This repository will help you understand the main concepts related to unit-test in Python. 
To do so, we are going to test a function that analyzes a text file content. The main features 
of this function are:
* return the number of line and characters of the input file  

### What will you learn ?
After reading this file, you will understand the following aspects:
* create a function ``analyse_text`` that returns a tuple with the number of lines and characters from an input file
* create a ``unittest`` class ``TextAnalysisTests`` that contains the following functions for testing the previous function
  - ``setUp``: runs before all test cases, and create our file to analysze.
  - ``tearDown``: executed after all the test cases, and will delete the previous text file created
  - ``test_function_runs``: runs the ``analyse_text`` function
  - ``test_line_count``: uses ``assertEqual`` to check the number of lines in the file
  - ``test_character_count``: also uses ``assertEqual`` to check the number of characters in the file
  - ``test_no_such_file_name``: uses ``assertRaises(IOError)`` to check that the proper exception is thrown by the ``analyse_text`` function
  - ``test_no_deletion`` uses ``assertTrue`` to check if the function deletes the input file at the end of the processing.  
  - ``__main__``, to run all the tests.  
  
