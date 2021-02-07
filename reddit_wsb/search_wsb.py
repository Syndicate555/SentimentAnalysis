from io import StringIO
import praw
import csv
from csv import reader
from praw.models import MoreComments
import pprint
import ibm_watson
from ibm_watson import ToneAnalyzerV3
import ibm_cloud_sdk_core.authenticators
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

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

key: str = "DEkSuJfnLXubq9NsV0vex0lJD0qslxDfwYJXUIpW2oD9"
url: str = "https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/0ac62d23-03cc-4096-8e5c-517e57c85884"

print(key)
print(url)
auth = IAMAuthenticator(key)
analyzer: ToneAnalyzerV3 = ToneAnalyzerV3(version='2017-09-21',
                                               authenticator=auth)
analyzer.set_service_url(url)

def analyze(text:str):
    print("Analyzing...  ", end="")
    res = analyzer.tone(text).get_result()
    document_tones = res["document_tone"]["tones"]
    emotions = (list(map(lambda x: x["score"], document_tones)))
    if not emotions:
        emotions = 0
    print(f"detected emotions: {emotions}")

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.new(limit=50):
    currPost = submission.title.encode('cp1252', errors='replace').decode('cp1252') 
    for stock in stockList:
        if (" " + str(stock) + " ") in currPost:
            print('\n******')
            print("STOCK: " + stock)
            print("TITLE: " + currPost)
            submission.comments.replace_more(limit=None)
            for top_level_comment in submission.comments:
                for second_level_comment in top_level_comment.replies:
                    analyze(top_level_comment.body.encode('cp1252', errors='replace').decode('cp1252'))


