from mxmapi import Musixmatch

mxm = Musixmatch("Your_API_Key")

result = mxm.track_get(track_spotify_id="6kwAbEjseqBob48jCus7Sz")
track =result["message"]["body"]["track"]