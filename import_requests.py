import requests
import random

def get_question():
    url = "https://the-trivia-api.com/v2/questions?categories=science&limit=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        question_data = response.json()[0]
        return question_data
    except requests.RequestException as e:
        print(f"Помилка при отриманні питання: {e}")
        return None

def main():
    question = get_question()
    if not question:
        return

    print("\nПитання з категорії 'Наука':")
    print(question['question']['text'])

    answers = question['incorrectAnswers'] + [question['correctAnswer']]
    random.shuffle(answers)

    for idx, answer in enumerate(answers, 1):
        print(f"{idx}. {answer}")

    try:
        user_choice = int(input("\nОберіть номер правильної відповіді: "))
        if user_choice < 1 or user_choice > len(answers):
            raise ValueError("Номер відповіді за межами списку.")
    except ValueError as e:
        print(f"Некоректний ввід: {e}")
        return

    user_answer = answers[user_choice - 1]
    if user_answer == question['correctAnswer']:
        print("Правильно! 🎉")
    else:
        print(f"Неправильно. 😞 Правильна відповідь: {question['correctAnswer']}")

if __name__ == "__main__":
    main()
