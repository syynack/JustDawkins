import praw
import time
import datetime
import os
import subprocess


CLIENT_ID = 'y2mOa57oaNxijA'
CLIENT_SECRET = 'TrA06FQTrHKCzaxTKnNgatDQ2P8'

def run_command(commands):
	for command in commands:
		subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		time.sleep(10)


def main():
	user_agent = praw.Reddit(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		user_agent='JustDawkins Meme Scraper'
	)

	get_command = 'wget {} --directory-prefix memes/'
	log_command = 'echo "{} MEME ADDED! {} has been added to the meme repo" >> meme.log'
	commit_command = 'git add memes/{}; git add meme.log; git commit -m "{} added to the meme repo"; git push'

	while True:
		for subreddit in ['me_irl', 'PrequelMemes', 'BlackPeopleTwitter', 'tinder']:
			for submission in user_agent.subreddit(subreddit).hot(limit=1):
				filename = submission.url.split('/')[-1]

				if not os.path.isfile("./memes/{}".format(filename)):
					run_command([
						get_command.format(submission.url),
						log_command.format(str(datetime.datetime.now()), filename),
						commit_command.format(filename, filename)
					])

		time.sleep(30)


if __name__ == '__main__':
	main()
