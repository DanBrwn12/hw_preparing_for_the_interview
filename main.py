
class Stack:
    def __init__(self, lst=None, element=None, str_balance=None):
        self.element = element
        self.lst = lst
        self.str_balance = str_balance

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def push(self):
        self.lst.append(self.element)

    def pop(self):
        self.lst.pop(-1)
        return self.lst[-1]

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)

    def check_balance_string(self):
        parentheses = ["(", ")"]
        square_brackets = ["[", "]"]
        brace = ["{", "}"]

        count_staples = {
            "parentheses_open": 0,
            "parentheses_close": 0,
            "square_brackets_open": 0,
            "square_brackets_close": 0,
            "brace_open": 0,
            "brace_close": 0
        }

        for staple in self.str_balance:
            if staple in parentheses[0]:
                count_staples["parentheses_open"] += 1
            elif staple in parentheses[1]:
                count_staples["parentheses_close"] += 1
            elif staple in square_brackets[0]:
                count_staples["square_brackets_open"] += 1
            elif staple in square_brackets[1]:
                count_staples["square_brackets_close"] += 1
            elif staple in brace[0]:
                count_staples["brace_open"] += 1
            elif staple in brace[1]:
                count_staples["brace_close"] += 1

        if (count_staples["parentheses_open"] == count_staples["parentheses_close"] and
                count_staples["square_brackets_open"] == count_staples["square_brackets_close"] and
                count_staples["brace_open"] == count_staples["brace_close"]):
            return "Сбалансировано"
        else:
            return "Несбалансированно"
