# gpa-obscuror

这是一个用于自动化评论和留言等行为需要辅助的 Python 包，旨在通过在文本中添加一些限制，有效防止被相关平台识别为机器爬虫行为。

## 特性

- 利用Python的基本语法，高性能处理中文文段
- 内置四个默认存在的引擎，可以随意切换
- 支持自定义引擎，一行代码完成注册

## 依赖

- Python 3.6+
- pypinyin~=0.50.0

## 快速使用

如果您不想从源代码安装，您可以直接安装发布到GitHub Releases页面的打包版本。

首先，下载最新的发布包 `gpa-obscuror-1.0.0.tar.gz` 从 [GitHub Releases](https://github.com/gupingan/gpa-obscuror/releases) 页面。

接着，您可以使用 pip 来安装下载的 `.tar.gz` 文件：

```bash
pip install /path/to/gpa-obscuror-x.x.x.tar.gz
```

其中 `x.x.x` 为您下载 `.tar.gz` 文件确版本。

确保替换 `/path/to/` 为您下载 `.tar.gz` 文件的实际路径。

安装完成后，您可以按照以下方式使用 `gpa-obscuror`：

```python
text = "惊了，你怎么知道我有三国演义的全集？"

# Step 1. 导入 obscuror 模块
from obscuror import obscuror

# Step 2. 使用 obscuror 加工评论
# obscuror对象参数：原文本，数量，模式
new_text = obscuror(text, 3)

# Step.3 使用 new_text.result 获取加工结果
print(new_text.result)
# print：惊了，你怎么知道我有三国演义的全集？庲醼哟
```

## 内置模式

- append：末尾追加模式，往文段末尾追加生僻字【缺省值】
- unison：同音替换模式，根据任意汉字的拼音替换为同音汉字，但无法限定声调
- non-cn: 汉字转音模式，随机将文段中的任意汉字替换为拼音
- insert：随机插入模式，在文段任意位置插入一个生僻字

```python
from obscuror import obscuror

text = "惊了，你怎么知道我有三国演义的全集？"

new_text = obscuror(text, 3, mode='unison')
print(new_text)
# print：惊了，你怎么庢道我有三国鷃冝的全集？

new_text = obscuror(text, 3, mode='non-cn')
print(new_text)
# print：惊le，你zěnme知道我有三国演义的全集？
```

## 拓展模式
可以先自定义一个 `module.py` 文件，其中需要导入 obscuror.engines.base 文件中的所有东西（建议这样做）。

> 创建 module.py

```python
# 这是一个可以随机插入生僻字的自定义引擎
from obscuror.engines.base import *

# 你需要继承 BaseEngine 类
class Insert(BaseEngine):
    name = '随机插入生僻字引擎'  # 一定要设置引擎名字，尽管你未使用
    
    # 重写 process 方法，设置返回值
    def process(self):
        rare_chars = [chr(random.randint(0x4E00, 0x9FD5)) for _ in range(self.count)]

        for char in rare_chars:
            insert_index = random.randint(0, len(self.text))
            self.text = self.text[:insert_index] + char + self.text[insert_index:]

        return self.text
```
> 回到`主文件`的代码中
```python
from obscuror import obscuror

text = "惊了，你怎么知道我有三国演义的全集？"

# 注册引擎，参数：模式名称，模块文件（多级需要使用.），引擎类名
obscuror.register_engine('insert', 'module', 'Insert')
new_text = obscuror(text, 3, mode='insert')
print(new_text)
# print：惊了，你怎么知道我有三坏国演撄义的全疠集？
```
以上是自定义引擎去处理文本的方法，比较简单，你只需要专注引擎的功能实现和性能提高。事实上，这个包中的内置引擎的本质也是如此实现下来的。

## 贡献

欢迎贡献！请为任何特性或修复创建一个分支，并提交一个合并请求。

## 许可证

本项目采用 MIT 许可证。请查看 [LICENSE](LICENSE) 文件以了解更多信息。

## 致谢

- 感谢所有贡献者（虽然没有=_=）的支持和贡献。
