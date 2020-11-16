from movies_storage import m_storage


def search_submenu():
    print("_"*48, "\n")
    print("MOVIE`S SEARCHING - SUBMENU :")
    print('''
    1 - search by movie title
    2 - search by director
    3 - search by year of premiere
    0 - back to main menu
    ''')


def submenu_search_title():
    title = input("Enter movie title: \n")
    print(f"\n*Searching movie by title: {title}")
    print("_" * 48)
    print("Found:\n")
    count = 1
    for i in (m_storage.search_movie_name(title)):
        print(f"{count}. {i}")
        count += 1
    input("\nPress [Enter] to continue.\n")


def submenu_search_director():

    director = input("Enter movie director: \n")
    print(f"\n*Searching movie by director: {director}")
    print("_" * 48)
    print("Found:\n")
    count = 1
    for i in (m_storage.search_movie_director(director)):
        print(f"{count}. {i}")
        count += 1
    input("\nPress [Enter] to continue.\n")


def submenu_search_year():
    year = input("Enter movie premiere year: \n")
    print(f"\n*Searching movie by director: {year}")
    print("_" * 48)
    print("Found:\n")
    count = 1
    for i in (m_storage.search_movie_year(year)):
        print(f"{count}. {i}")
        count += 1
    input("\nPress [Enter] to continue.\n")


def add_submenu():
    print("_"*48, "\n")
    print("ADDING MOVIE - SUBMENU :")
    print('''
    1 - add new movie to library
    0 - back to main menu
    ''')


def add_movie_storage():
    user_new_title = input("Enter title: ")
    user_new_director = input("Enter director: ")
    user_new_year = input("Enter movie premiere year: ")
    user_new_location = input("Enter movie location: ")
    print("\nData you`ve entered: ")
    print(f"""
    Title:          {user_new_title}
    Director:       {user_new_director}
    Year:           {user_new_year}
    Location:       {user_new_location}
    """)
    global add_title, add_director, add_year, add_location
    add_title = user_new_title
    add_director = user_new_director
    add_year = user_new_year
    add_location = user_new_location

"""
def add_to_storage_data():
    add_title = user_new_title
    add_director = user_new_director
    add_year = user_new_year
    add_location = user_new_location
    return add_title, add_director, add_year, add_location
"""


def show_all_movies():
    count = 1
    print("\nShowing all movies in storage:")
    print("_"*48)
    for movie in m_storage.movie_storage:
        print(f"{count} - {m_storage.search_movie_engine(movie)}")
        count += 1


while True:

    print("\nPiwan`s movies storage application - Gdynia 2020")
    print("_" * 48, "\n")
    print(""" MAIN MENU :\n
    1 - search a movie
    2 - add movie to storage
    3 - view all movies in storage
    0 - quit
    """)
    user_menu_select = (input("\nEnter your number according to the menu: \n"))

    if user_menu_select == "1":

        while True:
            search_submenu()
            print("_"*48)
            user_submenu_choice = (input("\nEnter your number according to the submenu: \n"))
            if user_submenu_choice == "1":
                submenu_search_title()
            elif user_submenu_choice == "2":
                submenu_search_director()
            elif user_submenu_choice == "3":
                submenu_search_year()
            elif user_submenu_choice == "0":
                break
            else:
                print("\nPlease select number only from menu: 1,2,3 or 0 !")

    elif user_menu_select == "2":
        while True:
            add_submenu()
            print("_"*48)
            user_submenu_choice = (input("\nEnter your number according to the submenu: \n"))
            if user_submenu_choice == "1":
                add_movie_storage()
                add_acceptation = input("\nEnter '1' to add new movie to storage or '0' to cancel operation: \n")
                if add_acceptation == '1':
                    print(add_title, add_director, add_year, add_location)
                    m_storage.add_movie_engine(add_title, add_director, add_year, add_location)
                    print("\nThe new movie has been successfully added to the library.")
                    input("Press [Enter] to continue.\n")

                elif add_acceptation == "0":
                    continue
            elif user_submenu_choice == "0":
                break
            else:
                print("\nPlease select number only from menu: 1 or 0 !")

    elif user_menu_select == "3":
        show_all_movies()
        print("_"*46)
        input("\nPress [Enter] to continue.\n")

    elif user_menu_select == "0":
        print("\nEnding program.")
        break

    else:
        print("\nPlease select number only from menu: 1,2,3 or 0 !")
