import requests


class User:
    def __init__(self, name, currancy=500, experience=5, level=1, achievements={}, inventory=[]):
        self.name = name
        self.achievements = achievements
        self.currancy = currancy
        self.experience = experience
        self.level = level
        self.inventory = inventory


class JamesCurrancyAPI:
    def get_user(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        user = User(name=data[username], currancy=data[username]["currancy"], achievements=data[username]['stats']['achievements'], items=data[username]['items'])
        return user

    def create_user(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()

        attributes = {"items": {}, "rewards": [], "currancy": 0, "score": {}, "stats": {"level": 1, "achievements": [], "experience": 0}}

        data[username] = attributes
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        #user = User(name=data[username], currancy=data[username]["currancy"], achievements=data[username]['stats']['achievements'], items=data[username]['items'])
        #return user

    def check_for_user(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        if username in data:
            return True
        else:
            return False
    
    def achievement_unlocked(self, username, achievement):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        data = data[username]['stats']['achievements']['achievement'] = achievement
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"success! {achievement} unlocked!"}

    def add_reward(self, username, reward):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        if username in data:
            data[username]["currancy"] += reward
        else:
            self.create_user(username)
            data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
            data[username]["currancy"] += reward
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"success! Rewarded {reward} to {username}"}
    
    def add_item(self, username, item):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        if username in data:
            data[username]["items"][item['name']] = {"item_info": item['item_info']}
        else:
            self.create_user(username)
            data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
            data[username]["items"][item['name']] = {"item_info": item['item_info']}
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"success! Rewarded {item} to {username}"}
    
    def get_level(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        level = data[username]['stats']['level']
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"the level is {level}"}

    def get_items(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        items = data[username]['items']
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"the items are {items}"}

    def get_currancy(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        currancy = data[username]['currancy']
        return {"name": username, "currancy": currancy}

    def get_achievements(self, username):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        achievements = data[username]['stats']['achievements']
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"the achievements are {achievements}"}

    def game_win(self, username, rewards, score, game):
        self.add_reward(username, rewards)
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        data[username]["score"][game] += score
        requests.post("https://store.ncss.cloud/group2/jamescurrancyapi", json=data)
        return {"message": f"Gave {username} {rewards} JamesCurrancy, player has a score of {score}"}


class RunAPI:
    def rewards(self, payload):
        api = JamesCurrancyAPI()

        name = payload['name']
        reward = payload['reward']

        api.add_reward(username=name, reward=reward)
        return {"name": name, "message": f"rewarded {reward}."}

    def item(self, payload):
        api = JamesCurrancyAPI()

        name = payload['name']
        item = payload['item']

        api.add_item(username=name, item=item)
        return {"name": name, "message": f"added {item} to {name} inventory"}

    def get_currancy(self, payload):
        api = JamesCurrancyAPI()
        try:
           name = payload['name']
        except KeyError:
            name = payload['author']

        return api.get_currancy(username=name)

    def get_items(self, username):
        api = JamesCurrancyAPI()
        return api.get_items(username=username)

    def game_win(self, payload):
        api = JamesCurrancyAPI()

        name = payload['name']
        rewards = payload['reward']
        score = payload['score']
        game = payload['game']

        return api.game_win(username=name, rewards=rewards, score=score, game=game)
#me=game)

