# create user agent to prevent 403 error
# google will block urllib based on the default user agent
# setting a new user agent prevents errors and allows
# mobile and desktop scraping
def user_agent(device):
    if device == 'mobile':
        ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) ' \
                    'Version/5.1 Mobile/9B179 Safari/7534.48.3'
        return ua_string
    elif device == 'desktop':
        ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                    'Chrome/60.0.3112.113 Safari/537.3'
        return ua_string
    else:
        ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                    'Chrome/60.0.3112.113 Safari/537.36'
        return ua_string
