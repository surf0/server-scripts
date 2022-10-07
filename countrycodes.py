import json

country_data = {}

with open(f'countrynames.json', 'r') as f:
    data = json.load(f)
    country_data = {key: value for key, value in sorted(
        data.items(), key=lambda x: x[1])}


def writeSQL(data):
    for code, name in data.items():
        sql = f'UPDATE ck_playerrank SET countryCode="{code.lower()}" WHERE country="{name}";\n'
        with open(f'countrycodes.sql', 'a') as f:
            f.write(sql)

# writeSQL(country_data)


# get countrynames.txt with: select distinct country from ck_playerrank;


my_countries = {}

country_fix = {'Czechia': 'Czech Republic'}

with open(f'countrynames.txt', 'r') as f:
    lines = [line.replace("|", "").strip() for line in f.readlines()]

    for country in lines:
        if country not in country_data.values():
            country2 = country.strip("The ")
            if country2 not in country_data.values():
                if country in country_fix:
                    country2 = country_fix[country]
                else:
                    print(country)
        else:
            country2 = country
        code = next((code for code, name in country_data.items()
                    if name == country2), None)

        my_countries[code] = country
my_countries = {key: value for key, value in sorted(
    my_countries.items(), key=lambda x: x[1])}

writeSQL(my_countries)
