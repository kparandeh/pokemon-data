import requests
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Load configurations at the start
system_config = load_config('configs/system_config.yml')
user_config = load_config('configs/user_config.yml')
api_base_url = system_config.get('api_base_url', 'default_url')

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.error(f"Error fetching data for {pokemon_name}: {e}")

except requests.exceptions.RequestException as e:
    logger.exception(f"Error fetching data for {pokemon_name}")
    return None

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


# Test the fetch data function
if __name__ == "__main__":
    pikachu_data = fetch_pokemon_data("pikachu")
    print(pikachu_data)


def get_pokemon_evolution(pokemon_name):
    """Fetch and display the evolution path for a given Pokemon"""
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/"
    try:
        species_response = requests.get(species_url)
        species_response.raise_for_status()
        species_data = species_response.json()
        evolution_chain_url = species_data['evolution_chain']['url']

        # Fetch the evolution chain
        evolution_response = requests.get(evolution_chain_url)
        evolution_response.raise_for_status()
        evolution_data = evolution_response.json()

        # Extract and format the evolution path
        path = []
        current_stage = evolution_data['chain']
        while current_stage:
            species_name = current_stage['species']['name']
            path.append(species_name.capitalize())  # Add current species to the path
            # Proceed to the next evolution stage, if any
            if current_stage['evolves_to']:
                current_stage = current_stage['evolves_to'][0]
            else:
                break
        return ' -> '.join(path)  # Correctly format and return the path
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving evolution path for {pokemon_name}: {e}")
        return "Evolution path not found."

# Test the evolution path function
if __name__ == "__main__":
    pokemon_name = "bulbasaur"  # Make sure this matches your function name
    evolution_path = get_pokemon_evolution(pokemon_name)  # This should match your function name as well
    print(f"Evolution path of {pokemon_name}: {evolution_path}")

