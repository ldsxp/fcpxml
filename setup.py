import os
import sys

from setuptools import setup, find_packages

version = '0.0.1'

"""
pip install -U fcpxml
pip --no-cache-dir install -U fcpxml

# 检查错误
# twine check dist/*

echo 使用 twine 上传到官方的pip服务器:
echo 在系统添加 TWINE_USERNAME 和 TWINE_PASSWORD 变量，不用输入用户名和密码
rmdir /S/Q build
rmdir /S/Q dist
python setup.py sdist bdist_wheel
echo 上传到PyPI:
twine upload dist/*

  "Development Status :: 1 - Planning",
  "Development Status :: 2 - Pre-Alpha",
  "Development Status :: 3 - Alpha",
  "Development Status :: 4 - Beta",
  "Development Status :: 5 - Production/Stable",
  "Development Status :: 6 - Mature",
  "Development Status :: 7 - Inactive",
  https://github.com/pypa/pypi-legacy/blob/1509d429fb4f2991156928e3f6fc5da0c1ee2095/trove.py
"""

# twine upload dist/* 使用 twine 上传
# 添加上传到 PyPI 的命令
if sys.argv[-1] == 'up':
    # os.system('rm -rf dist')
    # os.system('rm -rf build')
    os.system('rmdir /S/Q build')
    os.system('rmdir /S/Q dist')
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine check dist/*')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'dev':
    os.system('pip install wheel')
    os.system('pip install twine')
    sys.exit()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    # 名称
    name="fcpxml",
    # 版本
    version=version,
    # version=".".join(map(str, __import__('html2text').__version__)),
    # 关键字列表
    keywords=("fcpxml", "Final Cut Pro"),
    # 简单描述
    description="fcpxml 解析",
    # 详细描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    # 授权信息
    license="GNU GPL 3",

    # 官网地址
    url="https://github.com/ldsxp/fcpxml",
    # 程序的下载地址
    download_url="https://pypi.org/project/fcpxml",
    # 作者
    author="lds",
    # 作者的邮箱地址
    author_email="85176878@qq.com",

    # 需要处理的包目录（包含__init__.py的文件夹）
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    # 软件平台列表
    platforms="any",
    # 所属分类列表
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    # 需要安装的依赖包
    install_requires=[
    ],
    include_package_data=True,
    extras_require={'dev': ['wheel', 'twine', ]},
    python_requires='>=3.6',

    zip_safe=False
)
