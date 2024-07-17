class Song:
        
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}



    @classmethod
    def add_song_to_count(cls):
        cls.count+=1 # need to add cls here to reference class attribute

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] +=1
        else:
            cls.genre_count[genre] =1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist]=1

    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        # Song.artists.append(self.artist)
        # Song.add_to_genres()
        # Song.get_genre_count()
            
    def __repr__(self):
        return f"song name = {self.name}, artist={self.artist}, genre = {self.genre}"
    



    
    # @classmethod
    # def add_to_artists(cls):
    #     unique_artists = set(cls.artists)
    #     return unique_artists