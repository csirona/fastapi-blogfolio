from fastapi import APIRouter, Response,FastAPI, File, UploadFile
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.post_schema import PostSchema
from config.db import engine
from model.posts import posts
from typing import List, Union
from sqlalchemy import text

#define router
r = APIRouter()

#get all posts
@r.get("/api/post", response_model=List[PostSchema])
def get_posts():
    with engine.connect() as conn:
        result = conn.execute(posts.select()).fetchall()

    return result

#get all of posts by category
@r.get("/api/cat/{post_section}", response_model=List[PostSchema])
def get_posts_by_cat(post_section: str):
    with engine.connect() as conn:
        result = conn.execute(posts.select().where(posts.c.section==post_section)).fetchall()

    return result

@r.get("/api/post/{post_id}", response_model=PostSchema)
def get_post(post_id:int):
    with engine.connect() as conn:
        result = conn.execute(posts.select().where(posts.c.id==post_id)).first()

    return result

@r.post("/api/post" , status_code=HTTP_201_CREATED)
def create_post(data_post:PostSchema):
    with engine.connect() as conn:
        new_post = data_post.dict()
        conn.execute(posts.insert().values(new_post))

        return Response(status_code=HTTP_201_CREATED)

@r.put("/api/post/{post_id}")
def update(data_update: PostSchema, post_id: int):
    with engine.connect() as conn:
        conn.execute(posts.update().values(title=data_update.title,content=data_update.content).where(posts.c.id == post_id))

        result = conn.execute(posts.select().where(posts.c.id == post_id)).first()

        return result

@r.delete("/api/post/{post_id}",status_code=HTTP_204_NO_CONTENT)
def delete(data_update: PostSchema, post_id: int):
    with engine.connect() as conn:
        conn.execute(posts.delete().where(posts.c.id == post_id))


        return Response(status_code=HTTP_204_NO_CONTENT)
    
    
    
