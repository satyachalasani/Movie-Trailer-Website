import webbrowser
# Creation of the class named as movie


class Movie():
    # """ This class provides a movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # static varible
    # Creation of the constructor Movie

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
            # self is used for instance variables
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
            # Instance method to display the Movie trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
