# pip相关使用说明

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
