from pygal_maps_world import i18n

country_code_dict = i18n.COUNTRIES

def get_country_codes(desired_country_name):
    """Returns the 2-digit country code for the given country """
    for country_code, country_name in country_code_dict.items():
        if country_name == desired_country_name:
            return country_code
    return None

