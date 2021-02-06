# from psaw import PushshiftAPI
# api = PushshiftAPI()

# import datetime as dt

# start_epoch=int(dt.datetime(2017, 1, 30).timestamp())

# submissions = api.search_submissions(after=start_epoch,
#                             subreddit='wallstreetbets',
#                             filter=['url','author', 'title', 'subreddit'])

# for submission in submissions:
#     print(submission.title)
import praw
import pprint
reddit = praw.Reddit(
    client_id="lgFgtNzEtdL6UQ",
    client_secret="fDMBU3SlX6eVv5KceWvqc3VYNO54zg",
    user_agent="uottahack2021",
    username="Ok_Usual9821",
    password="uottahack2021"
)

print(reddit.read_only)

# assume you have a reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("wallstreetbets")

print(subreddit.display_name)  # output: redditdev

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=1):
    print(submission.title.encode('cp1252', errors='replace').decode('cp1252'))  # Output: the submission's title
    print(submission.url)    # Output: the URL the submission points to
    print()    

for top_level_comment in submission.comments:
    print(top_level_comment.body.encode('cp1252', errors='replace').decode('cp1252'))
    print()