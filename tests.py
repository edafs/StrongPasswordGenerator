import unittest;

class FunctionTests(unittest.TestCase):
    
    def testCanReadFile(self):
        from functions import _initWordContents;
        allWords = _initWordContents();
        self.assertEqual(len(allWords), 7776);

    def testCanGetWord(self):
        from functions import getWord;
        randomWord = getWord();
        self.assertTrue(randomWord);

    def testCanGetDelimiter(self):
        from functions import getDelimiter;
        randomDelimiter = getDelimiter();
        self.assertTrue(randomDelimiter);
        self.assertEqual(len(randomDelimiter), 1);