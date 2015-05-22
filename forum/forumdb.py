#
# Database access functions for the web forum.
#

import time
import psycopg2

DB = []
# ## Database connection
real_DB = psycopg2.connect("dbname=forum")
client = real_DB.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    all_posts = client.execute("select * from posts order by time")
    results = client.fetchall()
    posts = []
    for row in results:
      posts.append({'content': str(row[0]), 'time': str(row[1])})
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    client.execute("insert into posts values(%s)", (content,))
    real_DB.commit()
