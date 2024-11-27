from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接URL
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建一个基类，用于后续的模型类继承
Base = declarative_base()

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # 在这里导入所有定义的模型，以便在数据库中创建表 下面的一行
    # import yourapp.models
    Base.metadata.create_all(bind=engine)

# 请确保将 `username`、`password` 和 `dbname` 替换为你的 PostgreSQL 数据库的实际用户名、密码和数据库名。
# 同时，你需要安装 `SQLAlchemy` 和 `psycopg2`：
# pip install SQLAlchemy psycopg2