import betfairlightweight
from bonus_functions import hedge_bet
from datetime import date

"""
NOTE: THIS IS PURELY FOR EDUCATIONAL PURPOSES, NORMALLY YOUR SENSITIVE INFORMATION MUST BE ENCRYPTED AND
trading.login() USED INSTEAD OF trading.login.interactive()
"""

"""
INPUT DATA/READ FROM EXCEL
"""
USERNAME = "FILL IN USERNAME/EMAIL LOGIN"
PASSWORD = "FILL IN PASSWORD"
APP_KEY = "FILL IN APP_KEY"
locale = "FILL IN LOCALE"

home_team = "Ajax"
away_team = "Rangers"
market = "Over/Under 2.5 Goals"
outcome = "Under 2.5 Goals"
bet_size = 50
odds = 2.55
bet_type = "Qualifying bet"
date = date.today().isoformat()
continuous_output = True
verification = True

"""
RUN SCRIPT
"""
trading = betfairlightweight.APIClient(
    username=USERNAME,
    password=PASSWORD,
    app_key=APP_KEY,
    locale=locale)

trading.login_interactive()
if not trading.session_expired:
    print("---------------------------------------------------")
    print("YOU ARE NOW LOGGED IN!")
    print("---------------------------------------------------")

hedge = hedge_bet(
    betfair_client=trading,
    home_team=home_team,
    away_team=away_team,
    market=market,
    outcome=outcome,
    bet_type=bet_type,
    stake=bet_size,
    odds=odds,
    date=date,
    continuous_output=continuous_output,
    verification=verification)

if hedge:
    for key, val in hedge.items():
        print(key + ":", val)
    print("---------------------------------------------------")

trading.logout()
if trading.session_expired:
    print("YOU ARE NOW LOGGED OUT!")
    print("---------------------------------------------------")
