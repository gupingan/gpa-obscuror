"""File: base.py    Author: 顾平安"""
import random
import re
from abc import ABC, abstractmethod
from pypinyin import lazy_pinyin, pinyin


class BaseEngine(ABC):
    @property
    @abstractmethod
    def name(self):
        return '基础引擎'

    def __init__(self, text: str, count: int):
        self.text = text
        self.count = count

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @abstractmethod
    def process(self):
        return None
