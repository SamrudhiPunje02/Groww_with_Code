import pyshorteners

short = pyshorteners.Shortener()

actual_internet_url= "https://www.goibibo.com/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only+Goibibo&utm_term=%21SEM%21DF%21G%21Brand%21RSA%21108599293%216504095653%21602838584772%21e%21goibibo%21c%21&gad=1&gclid=Cj0KCQjwjt-oBhDKARIsABVRB0yM1d8C6yPkzqFUYDuPMGLGxuekLNC_bTGUw70ttOn7ArpYtrq_ZIMaAnAMEALw_wcB"

url_shortened= short.tinyurl.short(actual_internet_url)

print("The url is shorten to :", url_shortened)