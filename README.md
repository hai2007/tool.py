<p align='center'>
    <a href='https://hai2007.github.io/tool.py' target='_blank'>
        <img src='./logo.png'>
    </a>
</p>

# 💡 tool.py - python3常用的工具类方法汇总


## Issues
使用的时候遇到任何问题或有好的建议，请点击进入[issue](https://github.com/hai2007/tool.py/issues)，欢迎参与维护！

## 如何使用?

首先，我们默认你已经安装好```python3```并拥有了```pip```命令。

原则上安装了pip的环境都有setuptools,但并不影响你去尝试升级一下它：

```
pip install --upgrade setuptools
```

此外，我们还依赖一个简化将库发布到Pypi上流程的工具：

```
pip install --upgrade twine
```

这样，我们的前置工作就准备好了。

## 打包

在setup.py的同级目录下运行以下命令：

```
python setup.py sdist
```

## 发布

然后运行：

```
twine upload dist/*
```

## 使用

```
pip install basic-toolkit
```

如果希望安装特定版本：

```
pip install basic-toolkit==version
```

具体的使用你可以[查阅文档](https://hai2007.github.io/tool.py)哦~

开源协议
---------------------------------------
[MIT](https://github.com/hai2007/tool.py/blob/master/LICENSE)

Copyright (c) 2021-present [hai2007](https://hai2007.github.io/SweetHome/) 走一步，再走一步。
