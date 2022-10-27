from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,DateTime
from config.db import engine, meta_data
from datetime import datetime

posts = Table("posts",meta_data,
                Column("id", Integer,primary_key=True,autoincrement=True),
                Column("title",String(150),nullable=True,unique=True),
                Column("content",String(666),nullable=True),
                Column("created_at",DateTime,default=datetime.utcnow()))

meta_data.create_all(engine)