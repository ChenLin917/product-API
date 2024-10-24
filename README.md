## 環境需求
- Python 3.8
- Flask
- MySQL
- Docker

## 如何使用
1. Clone專案到本地：
    ```bash
    git clone https://github.com/ChenLin917/product-API.git

2. 進入專案目錄：
    ```bash
    cd <product-API>
    ```

3. 使用 Docker 啟動 MySQL 和 Flask API：
    - 確保您已經安裝 Docker 和 Docker Compose。
    - 在根目錄下運行以下命令來啟動：
      ```bash
      docker-compose up --build
      ```

4. 使用 Postman 或其他工具測試 API：
    - 獲取產品數據：
      (全部數據)
      GET http://localhost:5000/products

      (單一數據)
      GET http://localhost:5000/products/id
    
    - 添加新產品：
      POST http://localhost:5000/products
      Body:
      {
          "name": "Star",
          "code": "A-001",
          "category": "cloth",
          "size": "S, M",
          "unit_price": 200,
          "inventory": 20,
          "color": "Red, Blue"
      }

    - 修改新產品：(id為需要修改的索引值)
      PUT http://localhost:5000/products/id
      Body:
      {
          "name": "",
          "code": "A-001",
          "category": "cloth",
          "size": "S, M",
          "unit_price": 200,
          "inventory": 20,
          "color": "Red, Blue"
      }

    - 修改新產品：(id為需要刪除的索引值)
      DELETE http://localhost:5000/products/id


## Docker 設定
您可以使用 Docker 來啟動一個 MySQL 容器和 Flask API 容器。

1. 建立 Docker Compose 文件 (`docker-compose.yml`)：

    ```yaml
    services:
      web:
        build: .
        ports:
          - "5000:5000"
        environment:
          MYSQL_HOST: db
          MYSQL_USER: root
          MYSQL_PASSWORD: password
          MYSQL_DATABASE: flask_db
        depends_on:
          - db

      db:
        image: mysql:8.0
        environment:
          MYSQL_ROOT_PASSWORD: password
          MYSQL_DATABASE: flask_db
        ports:
          - "3307:3306"
        volumes:
          - db_data:/var/lib/mysql
          
    volumes:
      db_data:    
    ```

2. 建立一個 Dockerfile 用來建立 Flask 應用容器：

    **Dockerfile:**
    ```dockerfile
    ROM python:3.8-slim-buster

    WORKDIR /app

    COPY . .

    RUN pip3 install -r requirements.txt

    CMD ["python", "app.py"]
    ```

3. 安裝所需的 Python 環境，並創建 `requirements.txt` 文件：

    **requirements.txt:**
    ```
    Flask
    SQLAlchemy
    mysql-connector-python
    flask-sqlalchemy
    ```


