import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

# dotenv
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
HOST = os.getenv("MYSQL_HOST")
DATABASE = os.getenv("MYSQL_DATABASE")

# MySQL Connector/Pythonを使うためmysqlconnectorを指定する
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

# テーブルを定義する
Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animals'
    __table_args__ = (
        {
            "mysql_charset": "utf8mb4"
        }
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)


# テーブルを作成する
Base.metadata.create_all(engine)

# セッションを作成する
Session = sessionmaker(engine)
session = Session()

# データを追加する
cat = Animal(name='cat')
dog = Animal(name='dog')
session.add(cat)
session.add(dog)

session.commit()

# データを取得する
animals = session.query(
    Animal
).filter(
    Animal.name == "cat"
).count()
