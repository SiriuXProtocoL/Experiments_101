import webbrowser
import time
import random
while True:
    sites =  random.choice(["google.com","instagram.com","twitter.com","youtube.com"])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(4,7)
    time.sleep(seconds)