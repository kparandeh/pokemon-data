from analysis.analysis import fetch_pokemon_data, get_pokemon_evolution

def test_fetch_pokemon_data_valid():
    """Test fetching data for a valid Pokémon name."""
    result = fetch_pokemon_data('pikachu')
    assert result is not None
    assert 'abilities' in result

def test_get_pokemon_evolution_valid():
    """Test getting evolution path for a valid Pokémon name."""
    evolution_path = get_pokemon_evolution('charmander')
    assert 'charmeleon' in evolution_path.lower()
