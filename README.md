# 🧪 example_import_request

This is a simple Python script that sends a request to a **trivia API** and prompts the user to answer a science-related question. It demonstrates the use of HTTP requests, JSON parsing, and basic user interaction.

---

## 📌 Objective

- Fetch a science question from [the-trivia-api.com](https://the-trivia-api.com/)
- Display the question with shuffled multiple-choice answers
- Let the user select an answer from the console
- Show whether the answer is correct or not

---

## ⚙️ Implementation

The script consists of two main functions:

1. `get_question()` — sends a GET request to the API, parses the JSON response, and returns the question and answers.
2. `main()` — displays the question, receives the user's answer, checks if it's correct, and shows the result.

External libraries used:
- [`requests`](https://pypi.org/project/requests/) — for handling HTTP requests
- [`random`](https://docs.python.org/3/library/random.html) — for shuffling answer options

---

## ▶️ How to Run

Make sure to install the required dependencies:

```bash
pip install requests

Then run the script with:
python script.py

📎 Example Output
Science Question:
Which gas do plants absorb from the atmosphere?

1. Oxygen
2. Hydrogen
3. Carbon Dioxide
4. Nitrogen

Select the number of the correct answer: 3
Correct! 🎉

🔒 Error Handling
If the script fails to retrieve a question from the API, an error message is displayed.

If the user enters an invalid number, an appropriate warning is shown.

🧑‍💻 Author
Created as a learning example for practicing API usage and JSON handling in Python.
