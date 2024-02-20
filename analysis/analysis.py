import requests
import yaml
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to load configurations from YAML files
def load_config(config_path):
    with open(config_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            logger.error(f"Error loading YAML configuration from {config_path}: {e}")
            return None

# Load configurations at the start
system_config = load_config('configs/system_config.yml')
user_config = load_config('configs/user_config.yml')

def fetch_pokemon_data(pokemon_name):
    """Fetch details for a specific Pokemon."""
    api_base_url = system_config.get('api_base_url', 'https://pokeapi.co/api/v2')
    api_url = f"{api_base_url}/pokemon/{pokemon_name}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data for {pokemon_name}: {e}")
        return None

def get_pokemon_evolution(pokemon_name):
    """Fetch and display the evolution path for a given Pokemon."""
    api_base_url = system_config.get('api_base_url', 'https://pokeapi.co/api/v2')
    species_url = f"{api_base_url}/pokemon-species/{pokemon_name}/"
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
        return ' -> '.join(path)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error retrieving evolution path for {pokemon_name}: {e}")
        return "Evolution path not found."

# Example usage and testing
if __name__ == "__main__":
    # Test fetching Pokémon data
    pikachu_data = fetch_pokemon_data("pikachu")
    print(pikachu_data)

    # Test getting Pokémon evolution path
    bulbasaur_evolution_path = get_pokemon_evolution("bulbasaur")
    print(f"Evolution path of Bulbasaur: {bulbasaur_evolution_path}")
