import praw
import time
import subprocess


CLIENT_ID = 'y2mOa57oaNxijA'
CLIENT_SECRET = 'TrA06FQTrHKCzaxTKnNgatDQ2P8'

def main():
	user_agent = praw.Reddit(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		user_agent='JustDawkins Meme Scraper'
	)

	command = 'wget {} --directory-prefix ./memes/'

	while True:
		for submission in user_agent.subreddit('me_irl').hot(limit=1):
			get_link = subprocess.Popen(command.format(submission.url), shell=True, stdout=subprocess.PIPE)

		time.sleep(100000000)


if __name__ == '__main__':
	main()