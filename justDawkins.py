import praw
import time
import os
import subprocess


CLIENT_ID = 'y2mOa57oaNxijA'
CLIENT_SECRET = 'TrA06FQTrHKCzaxTKnNgatDQ2P8'

def run_command(command):
	subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)


def main():
	user_agent = praw.Reddit(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		user_agent='JustDawkins Meme Scraper'
	)

	get_command = 'wget {} --directory-prefix ./memes/'
	log_command = 'echo "MEME ADDED! {} has been added to the meme repo" >> meme.log'
	commit_command = 'git add ./memes/{}; git add memes.log; git commit -m "{} added to the meme repo"; git push'

	while True:
		for submission in user_agent.subreddit('me_irl').hot(limit=1):
			filename = submission.url.split('/')[-1]

			if not os.path.isfile("./memes/{}".format(filename)):
				run_command(get_command.format(submission.url))
				run_command(log_command.format(filename))
				run_command(commit_command.format(filename, filename))

		time.sleep(43200)


if __name__ == '__main__':
	main()