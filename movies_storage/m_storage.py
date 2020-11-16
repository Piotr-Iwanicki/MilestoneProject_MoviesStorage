
def search_movie_engine(movie_search):
    name = movie_search["name"]
    director = movie_search["director"]
    year = movie_search["year"]
    location = movie_search["location"]
    return f"Movie title: {name}, director: {director}, premiere: {year}, location: {location}."


def search_movie_name(title):
    search_results = []
    for movie in movie_storage:
        if movie["name"].find(title) != -1:
            search_results.append(search_movie_engine(movie))
    return search_results


def search_movie_director(director):
    search_results = []
    for movie in movie_storage:
        if movie["director"].find(director) != -1:
            search_results.append(search_movie_engine(movie))
    return search_results


def search_movie_year(year):
    search_results = []
    for movie in movie_storage:
        if movie["year"].find(year) != -1:
            search_results.append(search_movie_engine(movie))
    return search_results


def add_movie_engine(add_title, add_director, add_year, add_location):
    movie_storage.append({
        "name": add_title,
        "director": add_director,
        "year": add_year,
        "location": add_location
    })

    print("Adding movie!")
    return "\nAdding new movie to storage!\n"

movie_storage = [
    {
        "name": "The Matrix",
        "director": "Wachowskis",
        "year": "1994",
        "location": "3F-14"
    },
    {
        "name": "Star Trek",
        "director": "Abrams",
        "year": "2009",
        "location": "3S-18"
    },
    {
        "name": "Dune",
        "director": "Lynch",
        "year": "1984",
        "location": "3S-11"
    },
    {
        "name": "Star Trek Beyond",
        "director": "Abrams",
        "year": "2016",
        "location": "3S-19"
    },
    {
        "name": "Mission: Impossible – Fallout",
        "director": "Abrams",
        "year": "2018",
        "location": "3T-24"
    },
    {
        "name": "Overlord",
        "director": "Avery",
        "year": "2018",
        "location": "3H-09"
    }

]