def get_uuid(ign):
    import json
    import requests
    apiresponse = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(ign))
    data = json.loads(apiresponse.text)
    return data

def get_hypixel_data(uuid):
    import json, requests
    jsn = requests.get('https://api.hypixel.net/player?key=20f1f2a0-c2b7-47c6-8e58-4f01619ca8ac&uuid={}'.format(uuid))    
    data = jsn.json() # puts it all into a variable that can be managed by the program calling this function
    return data # gives it to another program

def played_bedwars(uuid):
    import json, requests
    jsn = requests.get('https://api.hypixel.net/player?key=20f1f2a0-c2b7-47c6-8e58-4f01619ca8ac&uuid={}'.format(uuid))    
    data = jsn.json() # puts it all into a variable that can be managed by the program calling this function
    return data['player']['games_played_bedwars_1'] # gives it to another program

def get_os():
    import sys
    platforms = {'linux' : 'Linux', 'linux1' : 'Linux', 'linux2' : 'Linux', 'darwin' : 'OS X', 'win32' : 'Windows'}
    if sys.platform not in platforms:
        platform = sys.platform
    else:
        platform = platforms[sys.platform]
    return platform

class undertale():
    def loadsandboxsteam(undertleini, file0):
        import os
        '''loads Undertale from Steam

        undertaleini = string. please lead to an ".ini" file with the correct parameters for "undertale.ini"
        
        file0 = leads to a custom file0 file.
        '''
        oldini = open(os.path.join('C:', 'Users', os.getlogin(), 'AppData', 'Local', 'UNDERTALE', 'undertale.ini'), "rt")
        oldfile0 = open(os.path.join('C:', 'Users', os.getlogin(), 'AppData', 'Local', 'UNDERTALE', 'file0'), "rt")
        steampath = str(input('Woah, woah, hold up! How do you access UNDERTALE? Where is SteamLibrary stored? '))
        

