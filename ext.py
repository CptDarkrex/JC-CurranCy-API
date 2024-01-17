import requests

item = requests.get("https://store.ncss.cloud/group2/shop").json()
attributes = {"url": "", "price": 500}
item["bid"] = attributes
requests.post("https://store.ncss.cloud/group2/shop", json=item)

#import requests

#class Good:
    #def __init__(self, name, url=0, price=500):
        #self.name = name
        #self.url = url
        #self.price = price

#class ShopAPI:
    
    #def create_item(self, itemname):
        #data = requests.get("https://store.ncss.cloud/group2/shop").json()

        #attributes = {"url": 0, "price": 500}

        #data[itemname] = attributes
        #requests.post("https://store.ncss.cloud/group2/shop", json=data)

        #item = Good(name=data[itemname], url=data[itemname]["url"], price=data[itemname]['price'])
        #return item

    #def create_user(self, username):
        #data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()

        #attributes = {"items": {}, "rewards": [], "currancy": 0, "score": {}, "stats": {"level": 1, "achievements": [], "experience": 0}}

        #data[username] = attributes
        #requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        

    #def game_win(self, itemname, url, price, game):
        #self.add_reward(itemname, rewards)
        #data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        #data[itemname]["score"][game] = score
        #requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        #return {"message": f"Gave {itemname} {rewards} JamesCurrancy, player has a score of {score}"}

#class Shop:
    #def items(self, payload):
        #api = ShopAPI()

        #name = payload['name']
        #url = payload['url']
        #price = payload['price']

        #return api.create_item(itemname=name)
        

#def game_win(self, payload):
        #api = JamesCurrancyAPI()

        #name = payload['name']
        #rewards = payload['reward']
        #score = payload['score']
        #game = payload['game']

        #return api.game_win(username=name, rewards=rewards, score=score, game=game)




    #def check_for_user(self, username):
        #data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        #if username in data:
            #return True
        #else:
            #return False