# create your simple Song class in this file

class Song:
    def __init__(self, title = "", artist = "", year = "", status = ""):
        self.title = title
        self.aritst = artist
        self.year = year
        self.status = status


    def __str__(self):
        return "{:40} by\t{:20}{} ".format(self.title, self.artist, self.year)
