import unittest
import clean_docs

file = 'test_clean_doc_function.txt'

class TestCleanDocFunction(unittest.TestCase):
    """测试函数clean_doc()

    Args:
        unittest (_type_): _description_
    """

    def test_clean_doc(self):
        """"""
        target_list = ["lemans", "france", "chongqing", "china", "apple",
        "banana", "watermellon"]
        list_doc = clean_docs.clean_doc(file)
        self.assertEqual(sorted(list_doc), sorted(target_list))

unittest.main()

    