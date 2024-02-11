  fp.seek(0)
    song = AudioSegment.from_file(fp, format = "mp3")
    play(song)