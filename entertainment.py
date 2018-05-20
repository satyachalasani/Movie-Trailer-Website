import fresh_tomatoes
import media

"""Creates four Movie objects, initialising these objects with title,
storyline, poster-image link, video trailer link"""

toy_story = media.Movie(
    "toy story", "a boy and his toy ",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

real_steel = media.Movie(
    "Real Steel", "robo fighting",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Real_Steel_Poster.jpg",
    "https://www.youtube.com/watch?v=vU3ZqtbIRPI"
    )

terminal = media.Movie(
    "Terminal", "A survival of a man in airport",
    "https://upload.wikimedia.org/wikipedia/en/8/86/"
    "Movie_poster_the_terminal.jpg",
    "https://www.youtube.com/watch?v=dgXyQUMRpj4"
    )

croods = media.Movie(
    "Croods", "A cave family called the Croods survives"
    "due to the overprotective nature of their stubborn"
    "stern patriarch, father, Grug",
    "https://upload.wikimedia.org/wikipedia/en/7/72/The_Croods_poster.jpg",
    "https://www.youtube.com/watch?v=4fVCKy69zUY"
    )

troy = media.Movie(
    "Troy", "portrays the battle between the ancient kingdoms"
    "of Troy and Sparta",
    " https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
    "https://www.youtube.com/watch?v=Voai-4GS848"
    )

grudge_match = media.Movie(
    "Grudge Match", "A pair of aging boxing rivalsare coaxed"
    "out of retirement to fight one final bout",
    "http://upload.wikimedia.org/wikipedia/""en/4/4a/Grudge_Match_Poster.jpg",
    "https://www.youtube.com/watch?v=1bQSOBJCPQE"
    )
# Creating an array with all the movies we want to add to our website
movies = [toy_story, real_steel, terminal, croods, troy, grudge_match]
# Calling the script that will create the HTML site based on our list'movies'
fresh_tomatoes.open_movies_page(movies)
