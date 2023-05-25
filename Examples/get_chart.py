from mxmapi import Musixmatch

mxm = Musixmatch("Your_API_Key")

result = mxm.chart_tracks_get("top")
data =result["message"]["body"]
print(data)