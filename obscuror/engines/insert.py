"""File: insert.py    Author: 顾平安"""
from .base import *


class Insert(BaseEngine):
    name = '随机插入生僻字引擎'

    def process(self):
        # 生成 self.count 个生僻字
        rare_chars = [chr(random.randint(0x4E00, 0x9FD5)) for _ in range(self.count)]

        # 将生僻字插入到随机位置
        for char in rare_chars:
            insert_index = random.randint(0, len(self.text))
            self.text = self.text[:insert_index] + char + self.text[insert_index:]

        return self.text
