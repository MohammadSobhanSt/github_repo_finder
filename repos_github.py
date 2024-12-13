import requests as re


username = input('enter a username to find its repositories: ')
url = f"https://api.github.com/users/{username}/repos"
response = re.get(url)


if response.status_code == 200:
	for item in response.json():
		print(item.get('name'))
    
else : 
	print(f"\n Username '{username}' not found on GitHub. Please try with another name... ")
