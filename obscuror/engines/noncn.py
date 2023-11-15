"""File: non-cn.py    Author: 顾平安"""
from .base import *


class NonCN(BaseEngine):
    name = '汉字转音引擎'

    def process(self):
        self.text = list(self.text)
        text_length = len(self.text)

        # 生成一个不重复的随机索引列表
        random_indexes = random.sample(range(text_length), min(self.count, text_length))

        # 替换指定索引处的汉字为拼音
        for index in random_indexes:
            self.text[index] = pinyin(self.text[index])[0][0]

        return ''.join(self.text)

