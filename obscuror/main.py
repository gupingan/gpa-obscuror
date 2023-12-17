"""File: main.py    Author: 顾平安"""
import importlib
from typing import Dict, Type
from .exceptions import *
from .engines import BaseEngine


class obscuror(object):
    __engines: Dict[str, Type[BaseEngine]] = {}

    def __init__(self, text, count, mode: str = 'append', shield: bool = True):
        self.text = str(text)
        self.count = int(count)
        self.mode = str(mode)
        self.shield = bool(shield)
        self.__load_engine()

    def __load_engine(self):
        # 注册默认存在的引擎
        self.register_engine('append', 'obscuror.engines', 'Append')
        self.register_engine('insert', 'obscuror.engines', 'Insert')
        self.register_engine('unison', 'obscuror.engines', 'Unison')
        self.register_engine('non-cn', 'obscuror.engines', 'NonCN')
        # 如果需要屏蔽违禁词
        if self.shield:
            self.register_engine('shield', 'obscuror.engines', 'Asterisk')

        # 判断当前选择模式是否已经注册
        if self.mode not in self.__engines:
            raise EngineNotFound(self.mode)

    @classmethod
    def register_engine(cls, mode, module, class_):
        mode, module, class_ = str(mode), str(module), str(class_)
        module = importlib.import_module(module)
        cls.__engines[mode] = getattr(module, class_)

    @property
    def engine_name(self):
        return self.__engines[self.mode].name

    @property
    def engines(self):
        return self.__engines

    @property
    def result(self):
        if self.shield:
            self.text = self.__engines['shield'](self.text, self.count).process()
        return self.__engines[self.mode](self.text, self.count).process()

    def __repr__(self):
        return f'obscuror-{self.mode}-{self.count}'

    def __str__(self):
        return self.result
