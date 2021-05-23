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
        

