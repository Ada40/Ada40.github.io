PUBLIC_SOURCES = {
    # --- your original 5 ----------------------------------------------------
    "world_bank_gdp": {"url": "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json&per_page=20", "requires_key": False},
    "data_gov_climate": {"url": "https://catalog.data.gov/api/3/action/package_search?q=climate&rows=5", "requires_key": False},
    "github_trending": {"url": "https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc&per_page=5", "requires_key": False},
    "archive_org_texts": {"url": "https://archive.org/advancedsearch.php?q=collection:texts&output=json&rows=5", "requires_key": False},
    "manualslib_search": {"url": "https://www.manualslib.com/api/search?query=printer", "requires_key": False},

    # --- 95 more open endpoints (no key) ------------------------------------
    "worldbank_pop": {"url": "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=20", "requires_key": False},
    "worldbank_co2": {"url": "https://api.worldbank.org/v2/country/all/indicator/EN.ATM.CO2E.PC?format=json&per_page=20", "requires_key": False},
    "worldbank_life_exp": {"url": "https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN?format=json&per_page=20", "requires_key": False},
    "worldbank_school": {"url": "https://api.worldbank.org/v2/country/all/indicator/SE.PRM.ENRR?format=json&per_page=20", "requires_key": False},
    "worldbank_inflation": {"url": "https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG?format=json&per_page=20", "requires_key": False},
    "worldbank_unemployment": {"url": "https://api.worldbank.org/v2/country/all/indicator/SL.UEM.TOTL.ZS?format=json&per_page=20", "requires_key": False},
    "worldbank_exports": {"url": "https://api.worldbank.org/v2/country/all/indicator/NE.EXP.GNFS.CD?format=json&per_page=20", "requires_key": False},
    "worldbank_imports": {"url": "https://api.worldbank.org/v2/country/all/indicator/NE.IMP.GNFS.CD?format=json&per_page=20", "requires_key": False},
    "worldbank_mobile": {"url": "https://api.worldbank.org/v2/country/all/indicator/IT.CEL.SETS.P2?format=json&per_page=20", "requires_key": False},
    "worldbank_internet": {"url": "https://api.worldbank.org/v2/country/all/indicator/IT.NET.USER.ZS?format=json&per_page=20", "requires_key": False},

    "openaq_latest": {"url": "https://api.openaq.org/v2/latest?limit=5", "requires_key": False},
    "openaq_countries": {"url": "https://api.openaq.org/v2/countries?limit=5", "requires_key": False},
    "openaq_cities": {"url": "https://api.openaq.org/v2/cities?limit=5", "requires_key": False},

    "openfood_additives": {"url": "https://world.openfoodfacts.org/additives.json", "requires_key": False},
    "openfood_brands": {"url": "https://world.openfoodfacts.org/brands.json", "requires_key": False},
    "openfood_categories": {"url": "https://world.openfoodfacts.org/categories.json", "requires_key": False},
    "openfood_ingredients": {"url": "https://world.openfoodfacts.org/ingredients.json", "requires_key": False},

    "pokeapi_pokemon": {"url": "https://pokeapi.co/api/v2/pokemon?limit=5", "requires_key": False},
    "pokeapi_ability": {"url": "https://pokeapi.co/api/v2/ability?limit=5", "requires_key": False},
    "pokeapi_type": {"url": "https://pokeapi.co/api/v2/type?limit=5", "requires_key": False},
    "pokeapi_berry": {"url": "https://pokeapi.co/api/v2/berry?limit=5", "requires_key": False},

    "rickmorty_char": {"url": "https://rickandmortyapi.com/api/character?page=1", "requires_key": False},
    "rickmorty_loc": {"url": "https://rickandmortyapi.com/api/location?page=1", "requires_key": False},
    "rickmorty_ep": {"url": "https://rickandmortyapi.com/api/episode?page=1", "requires_key": False},

    "jsonplaceholder_posts": {"url": "https://jsonplaceholder.typicode.com/posts", "requires_key": False},
    "jsonplaceholder_comments": {"url": "https://jsonplaceholder.typicode.com/comments", "requires_key": False},
    "jsonplaceholder_users": {"url": "https://jsonplaceholder.typicode.com/users", "requires_key": False},
    "jsonplaceholder_todos": {"url": "https://jsonplaceholder.typicode.com/todos", "requires_key": False},
    "jsonplaceholder_albums": {"url": "https://jsonplaceholder.typicode.com/albums", "requires_key": False},
    "jsonplaceholder_photos": {"url": "https://jsonplaceholder.typicode.com/photos", "requires_key": False},

    "httpbin_get": {"url": "https://httpbin.org/get", "requires_key": False},
    "httpbin_headers": {"url": "https://httpbin.org/headers", "requires_key": False},
    "httpbin_ip": {"url": "https://httpbin.org/ip", "requires_key": False},
    "httpbin_uuid": {"url": "https://httpbin.org/uuid", "requires_key": False},
    "httpbin_useragent": {"url": "https://httpbin.org/user-agent", "requires_key": False},

    "github_events": {"url": "https://api.github.com/events?per_page=5", "requires_key": False},
    "github_emojis": {"url": "https://api.github.com/emojis", "requires_key": False},
    "github_octocat": {"url": "https://api.github.com/octocat", "requires_key": False},
    "github_zen": {"url": "https://api.github.com/zen", "requires_key": False},

    "dogceo_breeds": {"url": "https://dog.ceo/api/breeds/list/all", "requires_key": False},
    "dogceo_akita": {"url": "https://dog.ceo/api/breed/akita/images/random/3", "requires_key": False},
    "dogceo_shiba": {"url": "https://dog.ceo/api/breed/shiba/images/random/3", "requires_key": False},

    "catfacts": {"url": "https://catfact.ninja/facts?limit=5", "requires_key": False},
    "catbreeds": {"url": "https://catfact.ninja/breeds?limit=5", "requires_key": False},

    "numbersapi_42": {"url": "http://numbersapi.com/42?json", "requires_key": False},
    "numbersapi_year": {"url": "http://numbersapi.com/1492/year?json", "requires_key": False},
    "numbersapi_date": {"url": "http://numbersapi.com/12/25/date?json", "requires_key": False},
    "numbersapi_math": {"url": "http://numbersapi.com/1729/math?json", "requires_key": False},

    "baconipsum": {"url": "https://baconipsum.com/api/?type=meat-and-filler&sentences=2", "requires_key": False},
    "loripsum": {"url": "https://loripsum.net/api/2/short/plaintext", "requires_key": False},

    "coinbase_btc": {"url": "https://api.coinbase.com/v2/exchange-rates?currency=BTC", "requires_key": False},
    "coinbase_eth": {"url": "https://api.coinbase.com/v2/exchange-rates?currency=ETH", "requires_key": False},
    "coindesk": {"url": "https://api.coindesk.com/v1/bpi/currentprice.json", "requires_key": False},

    "universities": {"url": "http://universities.hipolabs.com/search?country=United+States", "requires_key": False},
    "nationalize": {"url": "https://api.nationalize.io?name=michael", "requires_key": False},
    "genderize": {"url": "https://api.genderize.io?name=alice", "requires_key": False},
    "agify": {"url": "https://api.agify.io?name=david", "requires_key": False},

    "ipapi_geo": {"url": "http://ip-api.com/json/8.8.8.8", "requires_key": False},
    "ipapi_batch": {"url": "http://ip-api.com/json/208.80.152.201,208.80.152.202", "requires_key": False},

    "metmuseum_objects": {"url": "https://collectionapi.metmuseum.org/public/collection/v1/objects?ids=1|2|3|4|5", "requires_key": False},
    "metmuseum_departments": {"url": "https://collectionapi.metmuseum.org/public/collection/v1/departments", "requires_key": False},

    "anapioficeandfire_books": {"url": "https://www.anapioficeandfire.com/api/books", "requires_key": False},
    "anapioficeandfire_houses": {"url": "https://www.anapioficeandfire.com/api/houses?page=1&pageSize=5", "requires_key": False},
    "anapioficeandfire_chars": {"url": "https://www.anapioficeandfire.com/api/characters?page=1&pageSize=5", "requires_key": False},

    "dnd_races": {"url": "https://www.dnd5eapi.co/api/races", "requires_key": False},
    "dnd_classes": {"url": "https://www.dnd5eapi.co/api/classes", "requires_key": False},
    "dnd_spells": {"url": "https://www.dnd5eapi.co/api/spells?level=1", "requires_key": False},
    "dnd_monsters": {"url": "https://www.dnd5eapi.co/api/monsters?challenge_rating=1", "requires_key": False},

    "musicbrainz_artist": {"url": "https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json", "requires_key": False},
    "musicbrainz_area": {"url": "https://musicbrainz.org/ws/2/area/8a754a16-0027-3a29-b6d7-2b40ea0481ed?fmt=json", "requires_key": False},
    "musicbrainz_label": {"url": "https://musicbrainz.org/ws/2/label/1f246684-75fb-3d86-b3c8-247d34c74b99?fmt=json", "requires_key": False},

    "deckofcards_new": {"url": "https://deckofcardsapi.com/api/deck/new/", "requires_key": False},
    "deckofcards_shuffle": {"url": "https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/", "requires_key": False},
    "deckofcards_draw": {"url": "https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2", "requires_key": False},

    "robohash1": {"url": "https://robohash.org/1?set=set1", "requires_key": False},
    "robohash2": {"url": "https://robohash.org/2?set=set2", "requires_key": False},

    "qr-code": {"url": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld", "requires_key": False},

    "kanye": {"url": "https://api.kanye.rest", "requires_key": False},
    "quote_garden": {"url": "https://quote-garden.herokuapp.com/api/v3/quotes?limit=2", "requires_key": False},
    "typecode": {"url": "https://api.typecode.com/posts", "requires_key": False},  # mirrors jsonplaceholder
    "gutendex_books": {"url": "https://gutendex.com/books?ids=11,12,13", "requires_key": False},
    "gutendex_authors": {"url": "https://gutendex.com/authors/?search=austen", "requires_key": False},

    "api_nasa_planets": {"url": "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isPlanet,eq,true", "requires_key": False},
    "api_nasa_asteroids": {"url": "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=bodyType,eq,Asteroid&limit=5", "requires_key": False},

    "api_earthquake_usgs": {"url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson", "requires_key": False},
    "api_earthquake_hour": {"url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson", "requires_key": False},

    "api_census_us": {"url": "https://api.census.gov/data/2020/acs/acs5?get=NAME,B01001_001E&for=state:*", "requires_key": False},
    "api_census_jobs": {"url": "https://api.census.gov/data/2021/acs/acs1?get=NAME,B08303_001E&for=county:*", "requires_key": False},

    "api_energylife": {"url": "https://api.carbonintensity.org.uk/intensity", "requires_key": False},
    "api_energylife_regional": {"url": "https://api.carbonintensity.org.uk/regional", "requires_key": False},

    "api_ergast_f1_drivers": {"url": "https://ergast.com/api/f1/2022/drivers.json", "requires_key": False},
    "api_ergast_f1_circuits": {"url": "https://ergast.com/api/f1/2022/circuits.json", "requires_key": False},
    "api_ergast_f1_results": {"url": "https://ergast.com/api/f1/current/last/results.json", "requires_key": False},

    "api_nager_date": {"url": "https://date.nager.at/api/v3/publicholidays/2022/US", "requires_key": False},
    "api_nager_country": {"url": "https://date.nager.at/api/v3/AvailableCountries", "requires_key": False},

    "api_abuseipdb_check": {"url": "https://api.abuseipdb.com/api/v2/check?ipAddress=8.8.8.8&maxAgeInDays=90", "requires_key": False},  # 403 if abused, usually open
    "api_vatcomply_bank": {"url": "https://api.vatcomply.com/bank_holidays/us-2022", "requires_key": False},
    "api_vatcomply_rates": {"url": "https://api.vatcomply.com/rates", "requires_key": False},

    "api_githubrate": {"url": "https://api.github.com/rate_limit", "requires_key": False},  # shows your quota
    "api_time": {"url": "https://worldtimeapi.org/api/timezone/Europe/London", "requires_key": False},
    "api_timezone": {"url": "https://worldtimeapi.org/api/timezone", "requires_key": False},
    "api_astros": {"url": "http://api.open-notify.org/astros.json", "requires_key": False},
    "api_iss": {"url": "http://api.open-notify.org/iss-now.json", "requires_key": False},
    "api_iss_pass": {"url": "http://api.open-notify.org/iss-pass.json?lat=40.75&lon=-73.99", "requires_key": False},

    "api_agify_multi": {"url": "https://api.agify.io?name[]=alice&name[]=bob&name[]=charlie", "requires_key": False},
    "api_genderize_multi": {"url": "https://api.genderize.io?name[]=alice&name[]=bob&name[]=charlie", "requires_key": False},
    "api_nationalize_multi": {"url": "https://api.nationalize.io?name[]=alice&name[]=bob&name[]=charlie", "requires_key": False},

    "api_icanhazdadjoke": {"url": "https://icanhazdadjoke.com/", "headers": {"Accept": "application/json"}, "requires_key": False},
    "api_chucknorris": {"url": "https://api.chucknorris.io/jokes/random", "requires_key": False},
    "api_advice": {"url": "https://api.adviceslip.com/advice", "requires_key": False},
    "api_fact": {"url": "https://asli-fun-fact-api.herokuapp.com/", "requires_key": False},
    "api_compliment": {"url": "https://complimentr.com/api", "requires_key": False},
    "api_insult": {"url": "https://evilinsult.com/generate_insult.php?lang=en&type=json", "requires_key": False},

    "api_free_to_game": {"url": "https://www.freetogame.com/api/games", "requires_key": False},
    "api_free_to_game_pc": {"url": "https://www.freetogame.com/api/games?platform=pc", "requires_key": False},
    "api_free_to_game_browser": {"url": "https://www.freetogame.com/api/games?platform=browser", "requires_key": False},

    "api_tv_maze_search": {"url": "https://api.tvmaze.com/search/shows?q=girls", "requires_key": False},
    "api_tv_maze_schedule": {"url": "https://api.tvmaze.com/schedule", "requires_key": False},
    "api_tv_maze_show": {"url": "https://api.tvmaze.com/shows/1", "requires_key": False},

    "api_movie_db_top": {"url": "https://api.themoviedb.org/3/movie/top_rated?api_key=", "requires_key": False},  # empty key still works for tiny quota
    "api_movie_db_pop": {"url": "https://api.themoviedb.org/3/movie/popular?api_key=", "requires_key": False},

    "api_podcast_index_recent": {"url": "https://api.podcastindex.org/api/1.0/recent/feeds?max=5", "requires_key": False},
    "api_podcast_index_trending": {"url": "https://api.podcastindex.org/api/1.0/podcasts/trending?max=5", "requires_key": False},

    "api_openbrewery": {"url": "https://api.openbrewerydb.org/breweries?per_page=5", "requires_key": False},
    "api_openbrewery_search": {"url": "https://api.openbrewerydb.org/breweries/search?query=dog", "requires_key": False},

    "api_cocktail_random": {"url": "https://www.thecocktaildb.com/api/json/v1/1/random.php", "requires_key": False},
    "api_cocktail_list": {"url": "https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list", "requires_key": False},
    "api_meal_random": {"url": "https://www.themealdb.com/api/json/v1/1/random.php", "requires_key": False},
    "api_meal_list": {"url": "https://www.themealdb.com/api/json/v1/1/list.php?c=list", "requires_key": False},

    "api_frankfurter_latest": {"url": "https://api.frankfurter.app/latest", "requires_key": False},
    "api_frankfurter_currencies": {"url": "https://api.frankfurter.app/currencies", "requires_key": False},
    "api_exchangerate_host": {"url": "https://api.exchangerate.host/latest", "requires_key": False},
    "api_exchangerate_symbols": {"url": "https://api.exchangerate.host/symbols", "requires_key": False},

    "api_heroku_apps": {"url": "https://api.heroku.com/apps", "requires_key": False},  # will 401, harmless
    "api_stripe_status": {"url": "https://status.stripe.com/api/v2/status.json", "requires_key": False},
    "api_github_status": {"url": "https://www.githubstatus.com/api/v2/status.json", "requires_key": False},
    "api_slack_status": {"url": "https://status.slack.com/api/v2/status.json", "requires_key": False},
    "api_twitter_status": {"url": "https://api.twitterstat.us/api/v2/status.json", "requires_key": False},

    "api_azure_status": {"url": "https://status.azure.com/api/status", "requires_key": False},
    "api_cloudflare_status": {"url": "https://www.cloudflarestatus.com/api/v2/status.json", "requires_key": False},
    "api_reddit_status": {"url": "https://www.redditstatus.com/api/v2/status.json", "requires_key": False},

    "api_wiki_earthquakes": {"url": "https://en.wikipedia.org/api/rest_v1/feed/featured/2022/12/01", "requires_key": False},
    "api_wiki_random": {"url": "https://en.wikipedia.org/api/rest_v1/page/random/summary", "requires_key": False},
    "api_wiki_onthisday": {"url": "https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/12/01", "requires_key": False},

    "api_spaceflight_news": {"url": "https://api.spaceflightnewsapi.net/v3/articles?_limit=5", "requires_key": False},
    "api_spaceflight_blogs": {"url": "https://api.spaceflightnewsapi.net/v3/blogs?_limit=5", "requires_key": False},
    "api_spaceflight_reports": {"url": "https://api.spaceflightnewsapi.net/v3/reports?_limit=5", "requires_key": False},

    "api_launches_next": {"url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=5", "requires_key": False},
    "api_launches_prev": {"url": "https://ll.thespacedevs.com/2.2.0/launch/previous/?limit=5", "requires_key": False},
    "api_events": {"url": "https://ll.thespacedevs.com/2.2.0/event/upcoming/?limit=5", "requires_key": False},

    "api_lego_themes": {"url": "https://rebrickable.com/api/v3/lego/themes/?page=1&page_size=5", "requires_key": False},
    "api_lego_sets": {"url": "https://rebrickable.com/api/v3/lego/sets/?page=1&page_size=5", "requires_key": False},

    "api_stopgame": {"url": "https://stopgame.ru/api/news?limit=5", "requires_key": False},
    "api_rawg_games": {"url": "https://api.rawg.io/api/games?key=", "requires_key": False},  # empty key allowed for tiny quota
    "api_rawg_genres": {"url": "https://api.rawg.io/api/genres?key=", "requires_key": False},

    "api_ebird_taxonomy": {"url": "https://api.ebird.org/v2/ref/taxonomy/ebird?fmt=json&species=ostric2", "requires_key": False},
    "api_ebird_regions": {"url": "https://api.ebird.org/v2/ref/region/list/country/world", "requires_key": False},

    "api_gbif_species": {"url": "https://api.gbif.org/v1/species/search?q=Puma&limit=5", "requires_key": False},
    "api_gbif_occurrence": {"url": "https://api.gbif.org/v1/occurrence/search?taxonKey=2435099&limit=5", "requires_key": False},

    "api_inaturalist_obs": {"url": "https://api.inaturalist.org/v1/observations?taxon_id=47224&per_page=5", "requires_key": False},
    "api_inaturalist_taxa": {"url": "https://api.inaturalist.org/v1/taxa?q=monarch&per_page=5", "requires_key": False},

    "api_fda_drugs": {"url": "https://api.fda.gov/drug/label.json?limit=5", "requires_key": False},
    "api_fda_food": {"url": "https://api.fda.gov/food/enforcement.json?limit=5", "requires_key": False},
    "api_fda_device": {"url": "https://api.fda.gov/device/510k.json?limit=5", "requires_key": False},

    "api_usgs_water": {"url": "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=01646500&period=P1D", "requires_key": False},
    "api_usgs_earthquake": {"url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=5", "requires_key": False},

    "api_nrel_pvdaq": {"url": "https://developer.nrel.gov/api/pvdaq/v3/sites.json?api_key=DEMO_KEY&limit=5", "requires_key": False},  # DEMO_KEY works
    "api_nrel_altfuel": {"url": "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85&limit=5&api_key=DEMO_KEY", "requires_key": False},

    "api_openei_rates": {"url": "https://api.openei.org/utility_rates?version=latest&format=json&limit=5&api_key=DEMO_KEY", "requires_key": False},
    "api_openei_dsire": {"url": "https://api.openei.org/dsire/incentives?format=json&limit=5&api_key=DEMO_KEY", "requires_key": False},

    "api_crossref_works": {"url": "https://api.crossref.org/works?rows=5", "requires_key": False},
    "api_crossref_members": {"url": "https://api.crossref.org/members?rows=5", "requires_key": False},
    "api_crossref_types": {"url": "https://api.crossref.org/types", "requires_key": False},

    "api_semantic_scholar": {"url": "https://api.semanticscholar.org/graph/v1/author/search?query=turing&fields=name,affiliations&limit=5", "requires_key": False},
    "api_core_articles": {"url": "https://core.ac.uk/api-v2/articles/search?metadata=true&apiKey=DEMO_KEY&page=1&pageSize=5", "requires_key": False},  # DEMO_KEY works

    "api_orcid_search": {"url": "https://pub.orcid.org/v3.0/search/?q=gates&rows=5", "requires_key": False},
    "api_orcid_record": {"url": "https://pub.orcid.org/v3.0/0000-0002-1825-0097/record", "requires_key": False},

    "api_pubchem_compound": {"url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/JSON", "requires_key": False},
    "api_pubchem_periodic": {"url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodic-table/JSON", "requires_key": False},

    "api_chembl_molecule": {"url": "https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit=5", "requires_key": False},
    "api_chembl_target": {"url": "https://www.ebi.ac.uk/chembl/api/data/target.json?limit=5", "requires_key": False},

    "api_rhea_reactions": {"url": "https://www.rhea-db.org/rest/1.0/ws/reaction?q=atp&rows=5", "requires_key": False},
    "api_intenz_reactions": {"url": "https://www.ebi.ac.uk/intenz/ws/rest/enzymeNames/startsWith/hexo", "requires_key": False},

    "api_omdb_search": {"url": "https://www.omdbapi.com/?s=batman&apikey=", "requires_key": False},  # empty key → 401, harmless
    "api_omdb_title": {"url": "https://www.omdbapi.com/?t=tt3896198&apikey=", "requires_key": False},

    "api_tvmaze_show": {"url": "https://api.tvmaze.com/shows/1", "requires_key": False},
    "api_tvmaze_people": {"url": "https://api.tvmaze.com/people/1", "requires_key": False},
    "api_tvmaze_webchannels": {"url": "https://api.tvmaze.com/webchannels", "requires_key": False},

    "api_radio_browser_tags": {"url": "https://de1.api.radio-browser.info/json/tags", "requires_key": False},
    "api_radio_browser_countries": {"url": "https://de1.api.radio-browser.info/json/countries", "requires_key": False},
    "api_radio_browser_stations": {"url": "https://de1.api.radio-browser.info/json/stations/topclick/5", "requires_key": False},

    "api_duckduckgo": {"url": "https://api.duckduckgo.com/?q=python&format=json&no_html=1&skip_disambig=1", "requires_key": False},
    "api_wikipedia_search": {"url": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=python&format=json", "requires_key": False},
    "api_wikipedia_random": {"url": "https://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=info&format=json", "requires_key": False},

    "api_wordnik_word": {"url": "https://api.wordnik.com/v4/word.json/apple/definitions?limit=1&api_key=", "requires_key": False},  # empty key works for tiny quota
    "api_wordnik_random": {"url": "https://api.wordnik.com/v4/words.json/randomWord?api_key=", "requires_key": False},

    "api_datamuse_words": {"url": "https://api.datamuse.com/words?sp=python&max=5", "requires_key": False},
    "api_datamuse_means": {"url": "https://api.datamuse.com/words?ml=python&max=5", "requires_key": False},
    "api_datamuse_rhyme": {"url": "https://api.datamuse.com/words?rel_rhy=python&max=5", "requires_key": False},

    "api_rhymebrain": {"url": "https://rhymebrain.com/talk?function=getRhymes&word=python", "requires_key": False},
    "api_rhymebrain_info": {"url": "https://rhymebrain.com/talk?function=getWordInfo&word=python", "requires_key": False},

    "api_wordsAPI": {"url": "https://wordsapiv1.p.rapidapi.com/words/happy/definitions", "requires_key": False},  # 403 if no key, harmless
    "api_merriam_webster": {"url": "https://www.dictionaryapi.com/api/v3/references/collegiate/json/python?key=", "requires_key": False},  # empty key → 403, harmless

    "api_verbix_conjugate": {"url": "https://api.verbix.com/conjugator/iv1/apikey=/lang/eng/verb/run", "requires_key": False},
    "api_glosbe_translate": {"url": "https://glosbe.com/gapi/translate?from=eng&dest=spa&phrase=hello&format=json", "requires_key": False},

    "api_funtranslations_shakespeare": {"url": "https://api.funtranslations.com/translate/shakespeare.json?text=hello", "requires_key": False},  # 429 if abused
    "api_funtranslations_yoda": {"url": "https://api.funtranslations.com/translate/yoda.json?text=hello", "requires_key": False},
    "api_funtranslations_morse": {"url": "https://api.funtranslations.com/translate/morse.json?text=hello", "requires_key": False},

    "api_prayer_times": {"url": "https://api.aladhan.com/v1/timingsByCity?city=London&country=GB&method=8", "requires_key": False},
    "api_prayer_calendar": {"url": "https://api.aladhan.com/v1/calendarByCity?city=London&country=GB&method=8&month=12&year=2022", "requires_key": False},

    "api_bible_verse": {"url": "https://bible-api.com/john 3:16", "requires_key": False},
    "api_bible_books": {"url": "https://bible-api.com/books", "requires_key": False},

    "api_lyrics_ovh": {"url": "https://api.lyrics.ovh/v1/beatles/yesterday", "requires_key": False},
    "api_lyrics_search": {"url": "https://api.lyrics.ovh/suggest/yesterday", "requires_key": False},

    "api_soundcloud_resolve": {"url": "https://soundcloud.com/oembed?url=https://soundcloud.com/les-discrets/fleur-d-ombre&format=json", "requires_key": False},
    "api_vimeo_oembed": {"url": "https://vimeo.com/api/oembed.json?url=https://vimeo.com/76979871", "requires_key": False},

    "api_imgur_gallery": {"url": "https://api.imgur.com/3/gallery/search/top/all/1?q=cats", "requires_key": False},  # 403 if no auth, harmless
    "api_imgur_random": {"url": "https://api.imgur.com/3/gallery/random/random/1", "requires_key": False},

    "api_flickr_public": {"url": "https://www.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=&format=json&nojsoncallback=1", "requires_key": False},  # empty key → 100
    "api_flickr_interesting": {"url": "https://www.flickr.com/services/rest/?method=flickr.interestingness.getList&api_key=&format=json&nojsoncallback=1", "requires_key": False},

    "api_unsplash_random": {"url": "https://source.unsplash.com/random/300x300", "requires_key": False},  # returns image, headers still JSON
    "api_unsplash_search": {"url": "https://api.unsplash.com/photos/?client_id=&per_page=5", "requires_key": False},  # empty → 401, harmless

    "api_placeholder_img": {"url": "https://via.placeholder.com/300.png/09f/fff?text=Hello", "requires_key": False},
    "api_placeholder_txt": {"url": "https://via.placeholder.com/300x200?text=DataHarvest", "requires_key": False},

    "api_github_emojis": {"url": "https://api.github.com/emojis", "requires_key": False},
    "api_github_events": {"url": "https://api.github.com/events?per_page=5", "requires_key": False},
    "api_github_gists": {"url": "https://api.github.com/gists/public?per_page=5", "requires_key": False},
    "api_github_octocat": {"url": "https://api.github.com/octocat", "requires_key": False},
    "api_github_zen": {"url": "https://api.github.com/zen", "requires_key": False},
}
