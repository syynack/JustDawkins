import praw
import time
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

	while True:
		for submission in user_agent.subreddit('me_irl').hot(limit=1):
			run_command(get_command.format(submission.url))

		filename = submission.url.split('/')[-1]
		run_command(log_command.format(filename))

		time.sleep(43200)


if __name__ == '__main__':
	main()