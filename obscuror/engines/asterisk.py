"""File: asterisk.py    Author: 顾平安"""
from .base import *
from ..datas import BANNED_WORDS


class Asterisk(BaseEngine):
    name = '违禁词屏蔽引擎'

    def process(self):
        pattern = '|'.join(BANNED_WORDS)
        replace_asterisk = (lambda match: '*' * len(match.group()))
        return re.sub(pattern, replace_asterisk, self.text)
