#!/usr/bin/python
"""
Nice Tits Collector [NSFW]

Crawler used to collect all pics reddit user 'Only_Says_Nice_Tits' commented on.

Developed on Python 2.7.3

External Libraries:
	ReddiWrap: Reddit.com API wrapper
	Web: Web requests utility library, used by ReddiWrap

(c) Antonio Herraiz August/2013
"""
from ReddiWrap import ReddiWrap

reddit = ReddiWrap(user_agent='ReddiWrap')
import time # For sleep(), to avoid API rate limit
count = 0
pics = []
comments = reddit.get_user_comments('Only_Says_Nice_Tits')
if comments != None:
	while True:
		for comment in comments:
			# reddit.last_url will be like: http://reddit.com/r/funny/comments/1jkgf3/cbfmmzu.json
			post = reddit.get('/r/%s/comments/%s/%s' % (comment.subreddit, comment.link_id[3:], comment.id))
			url = post[0].url
			if 'imgur' in url and 'i.imgur' not in url:
				# TODO: http://imgur.com/ipv9GiY ==> http://i.imgur.com/ipv9GiY.xxx
				print('Transforming imgur URL')
			pics.append(url)
			print('Pic URL: %s' % (url))
			count += 1
		if count >= 100 or not reddit.has_next(): break
		time.sleep(2) # One request every 2 seconds.
		comments = reddit.get_next()
else:
	print('I can\'t retrieve stuff from reddit.com')
# TODO: do something with 'pics'

# EOF