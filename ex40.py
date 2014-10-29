class Song(object):
 def __init__(self, lyrics):
  self.lyrics = lyrics
  
 def sing(self):
  for line in self.lyrics:
   print line
   
happy_bday = Song(['AAAA',
'BBBBB',
'CCCCCC'])

another_song = Song(['JJJ',
'KKKKKK'])

happy_bday.sing()

print '-'*10

another_song.sing()