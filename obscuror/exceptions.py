"""File: exceptions.py    Author: 顾平安"""


class EngineNotFound(Exception):
    def __init__(self, mode):
        self.msg = f'{mode}模式指向不存在的引擎，无法使用'

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg
