# API to BlogFolio in FastApi

API to store and handle data of BlogFolio site

## Installation

### Dependencies
As this is a FastAPI, you must first have Python installed. [Python](https://www.python.org/)

Then create a virtual enviroment in the project directory ([Python-venv](https://docs.python.org/3/tutorial/venv.html))
```bash
python3 -m venv my_venv
```

To activate my_venv: 
```bash
source /my_venv/bin/activate       # for Linux
source /my_venv/Scripts/activate   # for de Windows
```
The'requirements.txt' file is used to install all dependencies in a recursive way.
```bash
pip install -r requirements.txt
```

### Data Base
In the file config/db.py have to be database settings

in this case it is use postgresql, thefore is necesary have postgres installed, create a database to fill in the next path

```bash
engine = create_engine("postgresql://postgres:password@localhost/posts")
```
or if you prefered  mysql
```bash
engine = create_engine("mysql+pymysql://cs:password@localhost/posts")
```
## Running

To run the project:
```bash
uvicorn app:app --reload
```
[Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python.

"app:app" set the main file as a app. In this case app.py is the main file.
"--reload" allow make changes in the project and is not necesary restart the server 

## Model
There are only one model:
Post:
    id: Optional[int]
    title: str
    content: str
    description:str
    created_at: Optional[date]=date.today() #default today's  date
    section: str
    tag: str
    gitlink: str

## Usage

Methods
##### Get all posts: endpoint="/api/post":
Return all posts in database
#### Get post by category:endpoint="/api/cat/{post_category}":
Give all posts that matchs with section=post_category}
#### Get a post:endpoint="/api/post/{post_id}":
Return a post that matchs with id={post_id}
#### Post a new post:endpoint="/api/post":
Create a new post
Return http status code 201
#### Put/Update a post replacing old data: endpoint="/api/post/{post_id}":
Update a post that matchs with id={post_id}
#### Delete a post:endpoint="/api/post/{post_id}":
Delete the post that matchs with id={post_id}
Return http status code 204

## About the project
This project was made to handle data with a database and be avaiable to make requests from blogFolio site.

More Information [API-BlogFolio](www.cristianosorio.com/projects/api-blogfolio)