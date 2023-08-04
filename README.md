# Exercise Tracker🏋️

A python program helps you track your exercises and the calories burned using the Nutritionix API for exercise information and the Sheety API for data storage.

## Requirements

- Python 3.x
- Ensure you have the required libraries installed by running: `pip install requests`

## Setup

1. Clone the repository to your local machine.

2. Set up environment variables:
   - `APP_ID`: Get your Nutritionix API app ID from [Nutritionix](https://developer.nutritionix.com/) and set it as an environment variable.
   - `APP_KEY`: Obtain your Nutritionix API app key.
   - `nutritionix_api_endpoint`: Set the API endpoint for Nutritionix.
   - `sheety_get_endpoint`: Set the API endpoint for retrieving data from Sheety [Sheety API](https://dashboard.sheety.co/).
   - `sheety_post_endpoint`: Set the API endpoint for adding data to Sheety.
   - `Authorization`: Set the Sheety API authorization token.

## Usage

1. Run the `main.py` script using the following command:
	`python main.py`

2. The program will prompt you to input the exercises you did. Enter the exercise names, you can write it like you're talking to a real person and it will fetch exercise details from the Nutritionix API, such as the calories burned during the exercise.

3. For each exercise entered, the program will display the name of the exercise and the corresponding calories burned.

4. It will then store the exercise details, along with the date, time, duration, and calories burned, in a Google Sheets document using the Sheety API.

## How It Works

1. **Nutritionix API:**
- The program uses the Nutritionix API to fetch exercise details based on the user's input. It sends a POST request with the exercise parameters (e.g., name, gender, weight, height, age) to the Nutritionix API.
- The API responds with exercise details, including the exercise name and calories burned.

2. **Sheety API:**
- For each exercise entered, the program stores the exercise details in a Google Sheets document using the Sheety API. It sends a POST request with the exercise data (e.g., date, time, exercise name, duration, calories burned) to the Sheety API endpoint.
- The Sheety API handles authentication using the provided authorization token.

3. **Data Presentation:**
- The program displays the exercise names and the corresponding calories burned to the user.

4. **Data Storage:**
- The program stores the exercise data in a Google Sheets document, making it easy for you to track your exercises and monitor your progress over time.

5. **Repeat Tracking:**
- The program can be run multiple times to track exercises on different days, and the data will be appended to the Google Sheets document for each session.
