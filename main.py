"""
Name: Chen Ruomeng
Date: 24/05/2018
Brief Project Description: Songs To Learn 2.0Songs
GitHub URL: https://github.com/CP1404assessment2/CP1404_Assessment2
"""
from kivy.app import App
from kivy.lang import Builder
from songlist import Songlist
from kivy.uix.button import Button
from operator import itemgetter

# Create your main program in this file, using the SonglistApp class
global songlist
class SongstolearnApp(App):
    def on_start(self):
        my_file = open("Songs.csv", "r")
        data = my_file.readlines()
        my_file.close()
        num_songlist = len(data)
        for i in range(0, num_songlist):
            songs = data[i].split("\n")
            songs = songs[0].split(",")
            songs[1] = str(songs[1])
            songs[2] = int(songs[2])
            for n in songs:
                if n == "":
                    songs.remove(n)
            songlist = Songlist()
            songlist.add_song(songs)
        Songlist.songlist.sort(key=itemgetter(2))

        for i in range(3):
            temp_button = Button(text=" ", background_color=[1, 2, 2, 2])
            temp_button.bind(on_release=self.press)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press(self, instance):
        count = 0
        count1 = 0
        count2 = 0
        title = instance.text
        for songs in Songlist.songlist:
            song_title = songs[0].split(",")
            if title == song_title[0]:
                songs[3] = "n"
        self.root.ids.entriesBox.clear_widgets()
        for songs in songlist.songlist:
            count += 1
            if songs[3] == "y":
                count1 += 1
                song_title1 = songs[0].split(",")
                temp_button = Button(text=song_title1[0], background_color=[1, 2, 2, 2])
                temp_button.bind(on_release=self.press)
                self.root.ids.entriesBox.add_widget(temp_button)
            else:
                count2 += 1
                song_title2 = songs[0].split(",")
                temp_button = Button(text=song_title2[0], background_color=[0.5, 0.5, 1, 1])
                temp_button.bind(on_release=self.press)
                self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.front_label.text = "To learn: {}, Learned:{}".format(str(count2),str(count1))
        self.root.ids.bottom_label.text = "Click songs to mark them as completed"

    def build(self):
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file("app.kv")
        return self.root

    def clear(self):
        self.root.ids.Title.text = ""
        self.root.ids.Author.text = ""
        self.root.ids.Year.text = ""

    def add_songs(self):
        new_song = Songlist()
        new_song.add_song(self.Title, self.Artist, self.Year)

    def list_songs(self):
        count = -1
        count1 = 0
        count2 = 0
        self.root.ids.entriesBox.clear_widgets()
        for songs in songlist.songlist:
            count += 1
            if songs[3] == "y":
                count1 += 1
                song_title1 = songs[0].split(",")
                temp_button = Button(text=song_title1[0], background_color=[1, 2, 2, 2])
                temp_button.bind(on_release=self.press)
                self.root.ids.entriesBox.add_widget(temp_button)
            else:
                count2 += 1
                song_title2 = songs[0].split(",")
                temp_button = Button(text=song_title2[0], background_color=[0.5, 0.5, 1, 1])
                temp_button.bind(on_release=self.press_completed)
                self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.front_label.text = "To learn: {}, Learned:{}".format(str(count2),str(count1))
        self.root.ids.bottom_label.text = "Click songs to mark them as completed"

    def press_completed(self,instance):
        title = instance.text
        for songs in songlist.songlist:
            song_title = songs[0].split(",")
            if title == song_title[0]:
                artist = songs[1]
                year = songs[2]
                break
        self.root.ids.bottom_label.text = "{} by {}, {}(completed)".format(title, artist, year)

    def new_songs(self):
        song_title = self.root.ids.Title.text
        song_artist = self.root.ids.Author.text
        song_year = self.root.ids.Year.text
        try:
            song_year = int(song_year)
            if song_year == float:
                self.root.ids.bottom_label.text = "ValueError, year cannot be float."
            elif song_year < 0:
                self.root.ids.bottom_label.text = "ValueError, year cannot be negative."
            else:
                song = []
                song.append(song_title)
                song.append(song_artist)
                song.append(song_year)
                song.append("y")
                songlist = Songlist()
                songlist.add_song(song)
                self.root.ids.bottom_label.text = "New song has been successfully added in list."
        except ValueError:
            self.root.ids.bottom_label.text = "ValueError, year must be number."

ReadingListApp().run()