# from psaw import PushshiftAPI
# api = PushshiftAPI()

# import datetime as dt

# start_epoch=int(dt.datetime(2017, 1, 30).timestamp())

# submissions = api.search_submissions(after=start_epoch,
#                             subreddit='wallstreetbets',
#                             filter=['url','author', 'title', 'subreddit'])

# for submission in submissions:
#     print(submission.title)
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

subreddit = reddit.subreddit("stocks")

with open("stocklist.txt") as f:
    stockList = f.readlines()
    stockList = [x.strip('\n') for x in stockList] 
# you may also want to remove whitespace characters like `\n` at the end of each line
#print(stockList)

# assume you have a Subreddit instance bound to variable `subreddit`
substring = "GME"
for submission in subreddit.new():#limit=100):
    currPost = submission.title.encode('cp1252', errors='replace').decode('cp1252') 
    #print(currPost)
    for stock in stockList:
        if str(stock) in currPost:
            print("STOCK: " + stock)
            print("TITLE: " + currPost)
    #if any(stock in currPost for stock in stockList):
        # print(stock)
        # print("TITLE: " + currPost)
    #if any(str(stock) in li for stock in stock_list):
    #print("Found: " + stock)
       # print(li)
    #print("POST TITLE: " + submission.title.encode('cp1252', errors='replace').decode('cp1252'))  # Output: the submission's title
    # print(submission.url)    # Output: the URL the submission points to
    #print()   
    # for top_level_comment in submission.comments:
    #     if isinstance(top_level_comment, MoreComments):
    #         continue
    #     print(top_level_comment.body.encode('cp1252', errors='replace').decode('cp1252'))
    # #print()
