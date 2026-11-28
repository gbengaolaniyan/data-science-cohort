song_title = "If You Like"
artist = "BNXN"

lyrics = """
I will really like to be your baby
But that's if, if you like
If you have somebody else ke sọ fun me
Break my heart, if you like
Oh-oh If you like, I go like
Me and you go somewhere nice on your time
Aeroplane, straight to Mykonos
But it all depends on if you really like
"""

print(f"{song_title} - {artist}".center(40, "="))
print()

for number, line in enumerate(lyrics.strip().split("\n"), start=1):
    print(f"{number:02d}. {line}")