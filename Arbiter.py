import challonge
import json

with open('config.json') as f:
    config = json.load(f)
    f.close()

KEY = config["key"]

challonge.set_credentials("DarthPhallus", KEY)

tournament = challonge.tournaments.show('qxmw7884')

print(tournament["id"])
