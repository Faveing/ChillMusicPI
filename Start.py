import os


class music():

	player = "mpv"
	dir = "Kikou"

	def play_all(self):
		os.system(self.player + " " + self.dir + "/*")

m = music()

while True:
	m.play_all()

