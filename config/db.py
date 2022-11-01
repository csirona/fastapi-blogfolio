from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:password@localhost/posts")

#prod
#engine = create_engine("mysql+pymysql://cs:password@localhost/posts")
meta_data=MetaData()