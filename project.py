import requests

while True:
    pokemon = input("Which Pokemon do you want to find?")
    pokemon = pokemon.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t{data['name']}")
        print(f"Height:{data['height']}")
        print(f"order:{data['order']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")
    exit = input("For Exit type yes[y] || no[n] :")
    if(exit == 'y'):
        break
    if(exit == 'n'):
        continue