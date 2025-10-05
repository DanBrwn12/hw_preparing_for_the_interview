# main.py
import unittest

from main import Stack

class TestStack(unittest.TestCase):
    def test_is_empty_true(self):
        lst = []
        st = Stack(lst)
        self.assertTrue(st.is_empty())
    def test_is_empty_false(self):
        lst = [1,2,3,4]
        st = Stack(lst)
        self.assertFalse(st.is_empty())

    def test_push_new_element(self):
        lst = ['asd']
        st = Stack(lst, 3)
        st.push()
        self.assertEqual(st.lst[-1], 3)

    def test_pop_element(self):
        lst = [12,'asd', 33, 22]
        st = Stack(lst)
        self.assertEqual(st.pop(), 33)

    def test_peek(self):
        lst = [12,'asd', 33, 22]
        st = Stack(lst)
        self.assertEqual(st.peek(), 22)

    def test_size(self):
        lst = [12,'asd', 33, 22]
        st = Stack(lst)
        self.assertEqual(st.size(), 4)

    def test_check_balance(self):
        str_balance = ['[([])((([[[]]])))]{()}',"(((([{}]))))", "{{[()]}}"]
        st = Stack(str_balance=str_balance)
        self.assertEqual(st.check_balance_string(), "Сбалансировано")

    def test_check_unbalance(self):
        str_balance = ["[[{())}]", "{{[(])]}}", "}{}"]
        for string in str_balance:
            st = Stack(str_balance=string)
            self.assertEqual(st.check_balance_string(), "Несбалансированно")