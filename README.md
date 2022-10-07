# server-scripts

## countrycodes

Generate SQL statements to fill countryCodes from country names.
(For [Surftimer](https://github.com/surftimer/SurfTimer) to get flags in [Surftimer-Web](https://github.com/surftimer/SurfTimer-Web))

1. get unique country names: `select distinct country from ck_playerrank;`
2. save them in `countrynames.txt`
3. run `python countrycodes.py`
4. if a country gets printed add it to `country_fix` and rerun python script

(Country list from http://country.io/names.json)
