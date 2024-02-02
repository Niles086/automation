import unittest
import os
import shutil

from your_script_file_name import create_folder, move_user_documents, sort_documents, parse_log_file

class TestAutomationScript(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        create_folder("temp_test_folder")

    def tearDown(self):
        # Clean up the temporary directory after each test
        shutil.rmtree("temp_test_folder", ignore_errors=True)

    def test_create_folder(self):
        create_folder("test_folder")
        self.assertTrue(os.path.exists("test_folder"))
    
    def test_move_user_documents(self):
        create_folder("temp_test_folder/user-docs/user")
        move_user_documents("temp_test_folder/user-docs/user", "temp_test_folder/temporary_folder")
        self.assertFalse(os.path.exists("temp_test_folder/user-docs/user"))
        self.assertTrue(os.path.exists("temp_test_folder/temporary_folder"))

    def test_sort_documents(self):
        create_folder("temp_test_folder/user-docs")
        create_folder("temp_test_folder/sorted_docs")
        with open("temp_test_folder/user-docs/test.log", 'w') as test_log:
            test_log.write("Test log content")
        sort_documents("temp_test_folder/user-docs", "temp_test_folder/sorted_docs")
        self.assertFalse(os.path.exists("temp_test_folder/user-docs/test.log"))
        self.assertTrue(os.path.exists("temp_test_folder/sorted_docs/logs"))
        self.assertTrue(os.path.exists("temp_test_folder/sorted_docs/logs/test.log"))

    def test_parse_log_file(self):
        create_folder("temp_test_folder/sorted_docs/logs")
        with open("temp_test_folder/sorted_docs/logs/test.log", 'w') as test_log:
            test_log.write("ERROR: Something went wrong\nWARNING: Be cautious\nINFO: This is just information")
        parse_log_file("temp_test_folder/sorted_docs/logs/test.log", "temp_test_folder/parsed_logs")
        self.assertTrue(os.path.exists("temp_test_folder/parsed_logs/errors.log"))
        self.assertTrue(os.path.exists("temp_test_folder/parsed_logs/warnings.log"))

if __name__ == '__main__':
    unittest.main()
