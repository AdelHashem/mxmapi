import unittest
from mxmapi import Musixmatch

track1_test = {
    "isrc": "EGA020501755",
    "track_spotify_id": "0dVuTFF29LqTatzfwoIwp6",
    "commontrack_id": 14135510,
    "track_id": 87657163,
    "album_id": 21110719,
    "album_name": "Allem Alby",
    "artist_id": 24432616,
    "commontrack_vanity_id": "Amr-Diab/Ally-el-Wadaa"
}

track1 = {
    "track_id": 87657163,
    "track_name": "Ally El Wadaa",
    "track_name_translation_list": [],
    "track_rating": 55,
    "commontrack_id": 14135510,
    "instrumental": 0,
    "explicit": 0,
    "has_lyrics": 1,
    "has_subtitles": 1,
    "has_richsync": 0,
    "num_favourite": 37,
    "album_id": 21110719,
    "album_name": "Allem Alby",
    "artist_id": 24432616,
    "artist_name": "Amr Diab"
}

class MusixmatchAPITest(unittest.TestCase):
    def setUp(self):
        # Initialize Musixmatch instance with your API key
        self.musixmatch = Musixmatch(API_key='1a5c1f4609e375a9784e88cb42fd084f')

    def test_track_get(self):
        response = self.musixmatch.track_get(track_isrc=track1_test.get("isrc"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

        response = self.musixmatch.track_get(track_spotify_id=track1_test.get("track_spotify_id"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

        response = self.musixmatch.track_get(commontrack_id=track1_test.get("commontrack_id"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

        response = self.musixmatch.track_get(commontrack_vanity_id=track1_test.get("commontrack_vanity_id"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

        response = self.musixmatch.track_get(track_id=track1_test.get("track_id"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

    def test_matcher_track_get(self):
        response = self.musixmatch.matcher_track_get(q_track="Ally El Wadaa", q_artist="Amr Diab", f_has_subtitles=1)
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

        response = self.musixmatch.matcher_track_get(q_track="Ally El Wadaa", q_artist="Amr Diab",
                                                     track_spotify_id=track1_test.get("track_spotify_id"))
        self.assertEqual(response["message"]["body"]["track"]["commontrack_id"], track1.get("commontrack_id"))

    def test_chart_artists_get(self):
        response = self.musixmatch.chart_artists_get(1, 20)
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_chart_tracks_get(self):
        response = self.musixmatch.chart_tracks_get(1, 20, "hot", 1)
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_track_search(self):
        response = self.musixmatch.track_search(1, 10, q_track="Ally el wadaa", q_artist="Amr Diab", f_has_lyrics=1)
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_track_lyrics_get(self):
        response = self.musixmatch.track_lyrics_get(track1_test["commontrack_id"])
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_track_snippet_get(self):
        response = self.musixmatch.track_snippet_get(track_id=track1_test.get("track_id"))
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_artist_get(self):
        response = self.musixmatch.artist_get(artist_id=track1_test.get("artist_id"))
        self.assertEqual(response["message"]["body"]["artist"]["artist_id"], track1_test.get("artist_id"))

    def test_artist_search(self):
        response = self.musixmatch.artist_search(q_artist="Amr Diab")
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_album_get(self):
        response = self.musixmatch.album_get(album_id=track1_test.get("album_id"))
        self.assertEqual(response["message"]["body"]["album"]["album_id"], track1_test.get("album_id"))

    def test_album_tracks_get(self):
        response = self.musixmatch.album_tracks_get(album_id=track1_test.get("album_id"), page=1, page_size=10)
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    """def test_track_richsync_get(self):
        response = self.musixmatch.track_richsync_get(track_id=track1_test.get("track_id"))
        self.assertEqual(response["message"]["header"]["status_code"], 200)"""

    def test_artist_related_get(self):
        response = self.musixmatch.artist_related_get(artist_id=track1_test.get("artist_id"), page=1, page_size=10)
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_matcher_subtitle_get(self):
        response = self.musixmatch.matcher_subtitle_get(q_track="Ally El Wadaa", q_artist="Amr Diab")
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_music_genres_get(self):
        response = self.musixmatch.music_genres_get()
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    def test_matcher_lyrics_get(self):
        response = self.musixmatch.matcher_lyrics_get(q_track="Ally El Wadaa", q_artist="Amr Diab")
        self.assertEqual(response["message"]["header"]["status_code"], 200)

    """def test_track_lyrics_translation_get(self):
        response = self.musixmatch.track_lyrics_translation_get(track_id=track1_test.get("track_id"), selected_language='en')
        self.assertEqual(response["message"]["header"]["status_code"], 200)"""



if __name__ == '__main__':
    unittest.main()
