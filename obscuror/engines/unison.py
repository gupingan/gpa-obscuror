"""File: unison.py    Author: 顾平安"""
from .base import *


class Unison(BaseEngine):
    name = '同音替换引擎'

    @staticmethod
    def create_pinyin_dict(start_unicode, end_unicode):
        pinyin_dict = {}
        for code in range(start_unicode, end_unicode + 1):
            char = chr(code)
            char_pinyin = lazy_pinyin(char)[0]
            if char_pinyin in pinyin_dict:
                pinyin_dict[char_pinyin].add(char)
            else:
                pinyin_dict[char_pinyin] = {char}
        return pinyin_dict

    pinyin_dic = create_pinyin_dict.__get__(object)(0x4E00, 0x9FD5)

    @staticmethod
    def replace_rare_char(text, pinyin_dict, count=1):
        text_list = list(text)
        valid_indices = [i for i, char in enumerate(text_list) if lazy_pinyin(char)[0] in pinyin_dict]

        if count > len(valid_indices):
            count = len(valid_indices)

        replace_indices = random.sample(valid_indices, count)

        for index in replace_indices:
            original_char = text_list[index]
            original_pinyin = lazy_pinyin(original_char)[0]
            rare_char_candidates = pinyin_dict[original_pinyin] - {original_char}
            if rare_char_candidates:
                text_list[index] = random.choice(list(rare_char_candidates))

        return ''.join(text_list)

    def process(self):
        return self.replace_rare_char(self.text, self.pinyin_dic, self.count)
