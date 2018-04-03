class Movie():
    # This class will hold all the info we need to store for our selected movies
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
