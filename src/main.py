"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from src.recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_profiles = {
        "High-Energy Melancholic Classical": {
            "genre": "classical",
            "mood": "melancholic",
            "energy": 1.0,
        },
        "Low-Energy Happy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.0,
        },
        "Energy-Only Midpoint Tie Probe": {
            "genre": "",
            "mood": "",
            "energy": 0.5,
        },
        "Rare Combo Lofi Energetic": {
            "genre": "lofi",
            "mood": "energetic",
            "energy": 1.0,
        },
        "Near-Tie Indie Rock Chill": {
            "genre": "indie rock",
            "mood": "chill",
            "energy": 0.82,
        },
        "Acoustic Preference Ignored": {
            "genre": "jazz",
            "mood": "happy",
            "energy": 0.37,
            "likes_acoustic": False,
        },
        "Ambient Intense Low-Energy Mismatch": {
            "genre": "ambient",
            "mood": "intense",
            "energy": 0.28,
        },
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}\n{'=' * len(profile_name)}\n")
        for index, rec in enumerate(recommendations, start=1):
            song, score, reasons = rec
            print(f"{index}. {song['title']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
