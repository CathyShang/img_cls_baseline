# 项目说明
爬取搜索引擎数据，并对数据进行筛选，完成获得可训练的单类别数据。

# 爬取数据
调用[Image-Downloader](https://github.com/sczhengyabin/Image-Downloader
)项目

# 安装环境
- python 3.7
- pytorch 1.9.0

```python
pip install -r requirements.txt
```

## 注意
- 建议安装selenium==2.48.0。最新的selenium已经放弃PhantomJS了，selenium<2.27.0也不含有PhantomJS，不然会遇到AttributeError
- 若pip自动下载有问题时，可尝试[pypi.org](https://pypi.org/project/)下载安装包进行手动下载

# 运行

运行初级数据筛选：
```
python img_primary_filter.py
```   
   
运行高级数据筛选：
```
python img_advanced_filter.py
```  