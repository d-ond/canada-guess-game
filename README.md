# Canadiam City Guessing Game
This is an interactive web-based game where players try to guess a hidden Canadian city based on feedback related to its name, population, province, and area, pulled from 2021 census data provided from Stats Canada.

## Gameplay
- Type in a city name in the input box.
- As you type, an autocomplete dropdown will appear. Select a city from the list or continue typing to refine your search.
- Click the "Submit Guess" button or press "Enter" to send your guess.
- View a detailed comparison of your guess with the hidden city based on:
  - Name
  - Location of province/territory
  - Population comparison
  - Area comparison
- Keep guessing until you find the correct city. When guessed correctly, the game will display a congratulatory message. You are able to play again by reloading the page.

## Technologies used
Frontend: HTML, CSS, JavaScript for interactive gameplay and responsive design.

Backend: Django for handling city data, processing guesses, and serving dynamic content.

Database: SQLite for storing and retrieving city information.

## Setup and Installation
To run this project locally, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/d-ond/canadian-city-guessing-game.git
cd canadian-city-guessing-game
```
2. Must have Django installed. If not, install them as follows:

```bash
pip install django
```
Run the Server:

```bash
python manage.py runserver
```

The game should now be accessible at http://127.0.0.1:8000/. Start typing city names to begin!
