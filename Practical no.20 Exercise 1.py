flashcards = {
    "Abundant": "Available in large quantities",
    "Benevolent": "Kind and generous",
    "Candid": "Honest and straightforward",
    "Diligent": "Hardworking and careful",
    "Eloquent": "Fluent and persuasive in speaking"
}
correct_answers = 0
total_questions = len(flashcards)
print("=== Vocabulary Flashcard Quiz ===")
for word, definition in flashcards.items():
    print("\nWord:", word)
    user_answer = input("Enter the definition: ")
    if user_answer.strip().lower() == definition.lower():
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
        print("Correct definition:", definition)
accuracy = (correct_answers / total_questions) * 100
print("\n=== Final Results ===")
print("Total questions:", total_questions)
print("Correct answers:", correct_answers)
print("Incorrect answers:", total_questions - correct_answers)
print(f"Accuracy score: {accuracy:.2f}%")
