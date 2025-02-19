# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
            }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    number_of_movies = len(user_data["watched"])
    if not number_of_movies:
        return 0.0

    total_rating = 0
    for watched_movie in user_data["watched"]:
        total_rating += watched_movie["rating"]
    return total_rating / number_of_movies

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_counter = {}
    for watched_movie in user_data["watched"]:
        genre = watched_movie["genre"]
        if genre in genre_counter:
            genre_counter[genre] += 1
        else:
            genre_counter[genre] = 1
    
    most_watched_genre, max_count = None, 0
    for genre, count in genre_counter.items():
        if count > max_count:
            most_watched_genre = genre
            max_count = count
    return most_watched_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched_movie_titles = list()
    for friend in user_data["friends"]:
        for friend_watched_movie in friend["watched"]:
            friends_watched_movie_titles.append(friend_watched_movie["title"])
    
    unique_watched = list()
    for watched_movie in user_data["watched"]:
        if watched_movie["title"] not in friends_watched_movie_titles:
            unique_watched.append(watched_movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    watched_moive_titles = list()
    for watched_movie in user_data["watched"]:
        watched_moive_titles.append(watched_movie["title"])

    friends_watched_movie_titles = set()
    friends_unique_watched = list()
    for friend in user_data["friends"]:
        for friend_watched_movie in friend["watched"]:
            if friend_watched_movie["title"] not in watched_moive_titles and friend_watched_movie["title"] not in friends_watched_movie_titles:
                friends_watched_movie_titles.add(friend_watched_movie["title"])
                friends_unique_watched.append(friend_watched_movie)
    return friends_unique_watched
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    accessible_hosts = user_data["subscriptions"]
    friends_unique_watched = get_friends_unique_watched(user_data)

    recommendation_list = list()
    for movie in friends_unique_watched:
        if movie["host"] in accessible_hosts:
            recommendation_list.append(movie)
    return recommendation_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)

    recommendation_list = list()
    for movie in friends_unique_watched:
        if movie["genre"] == favorite_genre:
            recommendation_list.append(movie)
    return recommendation_list

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    favorite_movies = user_data["favorites"]

    recommendation_list = list()
    for movie in unique_watched:
        if movie in favorite_movies:
            recommendation_list.append(movie)
    return recommendation_list
