from instapy import InstaPy
from instapy import smart_run

#username and pass here
my_username = 'expo_growth01'
my_password = '$MyExpo736!'


session = InstaPy(username = my_username,
				  password = my_password,
				  headless_browser = False)


# Follows the people that a given users are following
# The usernames can be either a list or a string
# The amount is for each account, in this case 30 users will be followed
# If randomize is false it will pick in a top-down fashion
#60 seconds for sleep_delay
#session specs
with smart_run(session):
	session.follow_user_followers(['faithcomedy', 'failvibe', 'midnightmemes'], 
								  amount = 15,
								  randomize = False,
								  sleep_delay = 180)

