import requests

def fetch_pokemon_data(pokemon_name):
    """Fetch details for a specific Pokemon"""
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(api_url)
        response.raise_for_status() # raise an error for bad response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None


# test
if __name__ == "__main__":
    pikachu_data = fetch_pokemon_data("pikachu")
    print(pikachu_data)