# python
## python包下载使用豆瓣源

>使用豆瓣源 

```
pip install -i https://pypi.doubanio.com/simple/ 
pip install -i https://pypi.doubanio.com/simple/ django==1.11.6
```

## 虚拟环境(在cmd下有效)
```
# 安装
pip install virtualenvwrapper-win
```

```
# 创建虚拟环境
mkvirtualenv [venv name]

退出虚拟环境 ： 
deactivate

# 删除
rmvirtualenv

workon [vir name] 进入对应的虚拟环境
```

## python3 下载xadmin: 
```
pip install git+git://github.com/sshwsfc/xadmin.git
```

## 在虚拟环境中使用pip命令生成依赖包文件：
```
(venv) $ pip freeze > requirements.txt
```
## 当需要创建这个虚拟环境的完全副本，可以创建一个新的虚拟环境，并在其上运行以下命令：
```
(venv) $ pip install -r requirements.txt
# 豆瓣源加速
pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
```

## 运行django项目 
```
python manage.py runserver
```

## python启动一个本地服务器
```
python -m http.server [8000]
```

