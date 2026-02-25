import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# .envから環境変数を読み込む
DATABASE_URL = os.environ['DATABASE_URL']
USE_SSL = os.getenv('USE_SSL', 'False').lower() == 'true'

connect_args = {}

# 本番の時(USE_SSL = Trueの時)だけCA Certificateを使う
if USE_SSL:
    connect_args['ssl'] = {
        'ca': './ca.pem'
    }


engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def db_connect():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()