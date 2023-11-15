"""File: append.py    Author: 顾平安"""
from .base import *


class Append(BaseEngine):
    name = '末尾追加引擎'

    def process(self):
        # 生成 self.count 个随机字符
        chars = [chr(random.randint(0x4E00, 0x9FFF)) for _ in range(self.count)]
        return f'{self.text}{"".join(chars)}'
