# NFT-GO后端服务
## 基于Vue3.0+Eelement-Plus+FastAPI+MongoDB的前后端分离的简易商城项目「后端部分」
## 运行环境
 - python 3.8.5
 - mongodb「需要新建名为NFTGO的数据库」
## 安装依赖
```
pip install -r requirements
```
## 启动方式
```
python run.py
```
## 简要说明
 - `main.py` 主要代码文件，API接口都写在里面「目前」
 - `models.py` 实体类模型，因为MongoDB的数据结构，需要为其定制特殊的实体类「说实话还没搞太懂」
 - `dbtest.py` 用于数据库连接检测，直接运行该文件，输出系统内全部数据库「如下图」则说明连接成功  
![image.png](https://tva1.sinaimg.cn/large/007e6d0Xgy1gqw388oixdj60bu02lgll02.jpg) 
## 特色功能
 - FastAPI会自动生成接口文档，可以直接测试接口，这个功能绝了👍
 - 进入方式：在启动的地址后面加上 `/docs`
 - ![image.png](https://tva1.sinaimg.cn/large/007e6d0Xgy1gqw3fkgh1gj60p10fl0tt02.jpg)