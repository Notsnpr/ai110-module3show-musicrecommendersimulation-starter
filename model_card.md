# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMixer 1.0.

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This recommender suggests songs a user may like.
It is for classroom exploration, not production use.
It assumes users can describe a genre, mood, and energy target.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

The model gives points for matching genre, mood, and energy.
Genre match adds 30 points.
Mood match adds 40 points.
Energy closeness adds up to 30 points.
Then songs are sorted by total score and the top results are returned.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

The dataset has 18 songs.
Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness.
Genres and moods are limited and not evenly represented.
Some labels appear once, so certain tastes are underrepresented.
This is a small sample dataset for learning.

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

The model works well when users provide clear genre and mood labels.
It usually surfaces songs that match the requested vibe.
The reason strings make ranking decisions easy to understand.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One weakness is that exact mood and genre matching can be too strict.
Rare combinations like lofi + energetic had fewer strong results.
This can create a filter bubble with repetitive recommendations.
The likes_acoustic preference is present but not used in scoring.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested seven profiles from src/main.py.
The profiles were High-Energy Melancholic Classical, Low-Energy Happy Pop, Energy-Only Midpoint Tie Probe, Rare Combo Lofi Energetic, Near-Tie Indie Rock Chill, Acoustic Preference Ignored, and Ambient Intense Low-Energy Mismatch.
For each profile, I checked the top-5 songs, scores, and reason text.
I also compared profile pairs to see what changed and why.
I was surprised that exact mood and genre matches often dominated ranking.
I was also surprised that Gym Hero appeared often for different profiles.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Add soft matching so related labels can get partial credit.
Use acoustic preference directly in scoring.
Add a diversity reranking step so top results are less repetitive.

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

My biggest learning moment was seeing how one weight change can completely reorder the top songs.
AI tools helped me move faster by suggesting test profiles, edge cases, and clearer wording for my explanations.
I still had to double-check AI suggestions by running the code and reading the score reasons line by line.
I was surprised that a very simple point system still felt like a real recommendation engine when the outputs matched each profile's vibe.
If I extend this project, I want to add soft tag matching, use acoustic preference in scoring, and add a diversity step so results are less repetitive.

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
