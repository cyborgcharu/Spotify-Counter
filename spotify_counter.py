import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set your Spotify API credentials
client_id = 'f94c757f02ed40709df24f0e67207975'
client_secret = '466c491adc484769960b9b54ecae88f1'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Tracklist and Artists
tracklist = [
    ("Flaunt It/Cheap", "Rae Sremmurd"),
    ("TUCA DONKA", "CURSEDEVIL"),
    ("mute", "Shygirl"),
    ("Raingurl", "Yaeji"),
    ("No Place", "RÜFÜS DU SOL"),
    ("CALMNESS", "MVTRIIIX"),
    ("side by side", "Logic1000"),
    ("Sociopathic Dance Queen", "Amaarae"),
    ("24k", "Tkay Maidza"),
    ("Selfish Soul", "Sudan Archives"),
    ("Groove District", "Starjunk95"),
    ("Thicc", "Shygirl"),
    ("South II", "Hxvrmxn"),
    ("ILUV", "Effy"),
    ("Colmillo", "Tainy"),
    ("City Girl", "Starjunk95"),
    ("Montagem Coral", "Nashirary"),
    ("This Place is Near You", "DVRST"),
    ("Zero Five Stars", "Coucou Chloe"),
    ("Delilah (Pull Me Out of This)", "Fred again.."),
    ("Atmosphere", "Fisher"),
    ("Money on the Dash", "Elley Duhé"),
    ("Empire Ants", "Gorillaz"),
    ("Stardust Circuit", "Starjunk95"),
    ("I Don’t Know", "Maryyx2"),
    ("Slay", "Eternxlkz"),
    ("Kota on a Plane", "Ninajirachi"),
    ("Real Truth", "J-E-T-S"),
    ("What You Like", "Logic1000"),
    ("Spotlight", "Childish Gambino"),
    ("Fein", "Travis Scott"),
    ("Crazy", "Doechii"),
    ("I Know", "Travis Scott"),
    ("World Princess Pt 2", "Grimes"),
    ("Andromeda Sunsets", "Starjunk95"),
]

# Function to get artist info
def get_artist_info(artist_name):
    result = sp.search(q='artist:' + artist_name, type='artist')
    if result['artists']['items']:
        artist = result['artists']['items'][0]
        return {
            'artist_name': artist['name'],
            'artist_id': artist['id'],
            'monthly_listeners': artist['followers']['total']
        }
    else:
        print(f"Artist not found: {artist_name}")
    return None

# Function to get track info
def get_track_info(track_name, artist_name):
    result = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track')
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        return {
            'track_name': track['name'],
            'track_id': track['id'],
            'stream_count': track['popularity']
        }
    else:
        print(f"Track not found: {track_name} by {artist_name}")
    return None

# Collecting data
data = []
for track, artist in tracklist:
    artist_info = get_artist_info(artist)
    if artist_info:
        track_info = get_track_info(track, artist_info['artist_name'])
        if track_info:
            data.append({
                'track_name': track,
                'artist_name': artist,
                'monthly_listeners': artist_info['monthly_listeners'],
                'stream_count': track_info['stream_count']
            })
        else:
            print(f"Track info not found for: {track} by {artist}")
    else:
        print(f"Artist info not found for: {artist}")

# Converting to DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame with all columns
with pd.option_context('display.max_columns', None):
    print(df)
