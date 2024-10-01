# Movie_Recommendation_Project

```markdown
# Movie Recommendation Project

## Overview
This project is a movie recommendation system built with Django. It utilizes the **Jaccard Similarity** algorithm to recommend movies to users based on their viewing history.

## Features
- Personalized movie recommendations
- Jaccard Similarity calculation
- User viewing history tracking
- Movie database management

## Tech Stack
- **Backend:** Django
- **Database:** SQLite (default)
- **Algorithm:** Jaccard Similarity
- **Frontend:** HTML, CSS

## Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/Samilincoln/Movie_Recommendation_Project.git
cd movie-recommendation
```

### 2. Create a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run Migrations:
```bash
python manage.py migrate
```

### 5. Create a Superuser:
```bash
python manage.py createsuperuser
```

### 6. Run the Server:
```bash
python manage.py runserver
```

## Usage
1. Access the application in your browser at `http://127.0.0.1:8000/`.
2. Log in with the superuser account.
3. Add movies via the Django admin panel or the web interface.
4. As users interact with the movie database, they will receive personalized recommendations based on their viewing history.

## How it Works

- **Jaccard Similarity**: The system uses the Jaccard Similarity to calculate similarity between users' movie preferences. Jaccard Similarity between two users `A` and `B` is given by:
  
  ```
  J(A, B) = |A ∩ B| / |A ∪ B|
  ```

  Where `A` and `B` are sets of movies watched by two users.

- The system recommends movies based on the highest similarity scores between users and their shared preferences.

## Models

- **Movie**: Represents the movies in the system, storing attributes like title, genre, description, and release year.
- **UserHistory**: Tracks each user's watched movies and stores user-specific data for personalized recommendations.

## API Endpoints

- **/movies/**: Displays all movies.
- **/recommendations/**: Shows personalized movie recommendations for logged-in users.

## Future Enhancements

- Integrate collaborative filtering for better recommendations.
- Implement a movie rating system.
- Introduce machine learning models to enhance recommendation accuracy.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

```

