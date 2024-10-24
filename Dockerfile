# 引用 3.8 debian buster 發行版
FROM python:3.8-slim-buster
# Docker 命令的工作路徑 路徑若不存在會自動創建
WORKDIR /app
# COPY <本地路徑> <目標路徑> 本地路徑 : 代表本地文件 "." 代表程序跟目錄下的所有文件  目標路徑 : Docker 鏡像中的路徑 "." 代表當前的工作路徑 這裡指定是app目錄
COPY . .
# install 所需的環境
RUN pip3 install -r requirements.txt

EXPOSE 5000

# CMD["可執行文件", "參數1", "參數2"...]

CMD ["python", "app.py"]
