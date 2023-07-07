def quiz():
  print("Welcome to Basic Python Quiz For Beginners 🤓")
  answer = input("Are you ready to play the Quiz ? (y/n) :")
  score = 0
  total_questions = 6

  if answer.lower() == "y":
    answer = input("Question 1: What is a correct syntax to output \"hello world\" in Python?")
    if answer.lower() == 'print("hello world")':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

    answer = input("Question 2: How do you insert (this is a comment) COMMENTS in Python code?")
    if answer.lower() == '#this is a comment':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

    answer = input("Question 3: How do you create a variable with the numeric value 5?")
    if answer.lower() == 'x = 5':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

    answer = input("Question 4: What is the correct file extension for Python files?")
    if answer.lower() == '.py':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

    answer = input("Question 5: In Python, \"Hello\", is the same as \"Hello\"? (true/false)")
    if answer.lower() == 'false':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

    answer = input("Question 6: Which operator is used to multiply numbers?")
    if answer.lower() == '*':
      score += 1
      print('Correct ✅')
    else:
      print('Wrong Answer ❌')

  print(f"Thank you for Playing this small quiz game, you attempted {score} questions correctly!")
  mark = (score / total_questions) * 100
  print(f"Marks obtained: {mark}")
  print("BYE 🫶")

if __name__ == "__main__":
  quiz()
