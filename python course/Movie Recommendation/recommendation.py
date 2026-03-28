import time, pandas as pd
import textblob as TextBlob

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print("we couldn't find the file")


def dots():
    for _ in range(3): print(".", end="", flush=True); time.sleep(0.5)

def senti(p): return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."

def show(recs, name):
    print(f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})")

def get_genre():
    print("Available genres:")
    for i, g in enumerate(genres, 1): print(f"{i}. {g}")
    print()
    while True:
        x = input("Enter genre name or number").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres): return genres[int(x)-1]
        x = x.title()
        if x in genres: return x
        print("invalid input, try again")
        
def get_rating():
    while True:
        input("Enter a minimum rating (7.6-9.3) or 'skip'").strip()
        if x.lower == 'skip':
            return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            print("rating out of range, try again")
        except ValueError:
            print("Invalid input. Try again.\n")
            
            
        

print("Welcome to you personal ai movie assistant")
name = input("What is your name")
print(f"hello {name}, let's find the perfect movie for you")

genre = get_genre
mood = input("How do you feel today(describe your mood)?").strip()
print("analyzing mood", flush= True); dots()
mp = TextBlob(mood).sentiment.polarity
md = "positive 👍" if mp>0 else "negative 👎" if mp<0 else "neutral 😐"
print(f"your mood is {md} (Polarity {mp:.2f})")

rating = get_rating()
print(f"\nFinding movies for {name}", end="", flush=True); dots()
recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
print(recs + "\n") if isinstance(recs, str) else show(recs, name)

while True:
    a = input("\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "no":
        print(f"\nEnjoy your movie picks, {name}! 🎬🍿\n"); break
    if a == "yes":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
        print(recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print("Invalid choice. Try again.\n")



