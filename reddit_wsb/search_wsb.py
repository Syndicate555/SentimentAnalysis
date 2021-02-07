from io import StringIO
import praw
import csv
from csv import reader
from praw.models import MoreComments
import pprint
reddit = praw.Reddit(
    client_id="lgFgtNzEtdL6UQ",
    client_secret="fDMBU3SlX6eVv5KceWvqc3VYNO54zg",
    user_agent="uottahack2021",
    username="Ok_Usual9821",
    password="uottahack2021"
)

subreddit = reddit.subreddit("pennystocks")

with open("stocklist.txt") as f:
    stockList = f.readlines()
    stockList = [x.strip('\n') for x in stockList] 

# assume you have a Subreddit instance bound to variable `subreddit`
substring = "GME"
for submission in subreddit.new(limit=500):
    currPost = submission.title.encode('cp1252', errors='replace').decode('cp1252') 
    for stock in stockList:
        if (" " + str(stock) + " ") in currPost:
            print('\n******')
            print("STOCK: " + stock)
            print("TITLE: " + currPost)
            print('******\n')
            submission.comments.replace_more(limit=None)
            for top_level_comment in submission.comments:
                for second_level_comment in top_level_comment.replies:
                    print(top_level_comment.body.encode('cp1252', errors='replace').decode('cp1252'))

