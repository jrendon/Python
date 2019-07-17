# ---------------------------------------------------------
    # Search Twitter via a Hashtag and then like the post
    # Thank you Interwebs for coding help and troubleshooting hints
    # Requirements:
    # Python is a given
    # Firefox, you could use Chrome but I haven't tested it yet
    # Gecko Driver: https://github.com/mozilla/geckodriver/releases - Extract and place exe in root of Python 
        # Gecko is a Proxy for using W3C WebDriver compatible clients to interact with Gecko-based browsers.
    # Selenium (webdriver): Simply 'pip install selenium', this allows Python to install it for you.
# ---------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

strUserName = 'name@email.com'
# strUserPass = 'PassWord!' 
strUserPass = getpass() # So the password isn't plain text but it's a choice now
# strHashTag = 'HashtagName'
strHashTag = input('HashTag? ')

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)') 
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                print(link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)     

# Create Instance
BotCrawl = TwitterBot(strUserName, strUserPass)
BotCrawl.login()
BotCrawl.like_tweet(strHashTag)