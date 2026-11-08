# Project 4: The General Knowledge Quiz
# DecodeLabs - Python Programming (Control Flow, State Management, Input Sanitization)

print("=" * 40)
print("   Welcome to the General Knowledge Quiz!")
print("=" * 40)
print("Answer 3 questions. You get +1 point for each correct answer.\n")

# State initialization (integer, so cumulative math is reliable)
score = 0

# ---------- Question 1 ----------
answer = input("Q1. What is the capital of France? ")   # Ask & Capture
answer = answer.strip().lower()                          # Sanitize
if answer == "paris":                                    # Evaluate
    print("Correct! Well done.")                         # Execute (success)
    score += 1
else:
    print(f"Wrong! The correct answer is: paris (you said: '{answer}')")  # Execute (failure)

# ---------- Question 2 ----------
answer = input("\nQ2. Which planet is known as the Red Planet? ")  # Ask & Capture
answer = answer.strip().lower()                                      # Sanitize
if answer == "mars":                                                 # Evaluate
    print("Correct! Well done.")                                     # Execute (success)
    score += 1
else:
    print(f"Wrong! The correct answer is: mars (you said: '{answer}')")  # Execute (failure)

# ---------- Question 3 ----------
answer = input("\nQ3. How many continents are there on Earth? (type a number) ")  # Ask & Capture
answer = answer.strip().lower()                                                    # Sanitize
if answer == "7":                                                                  # Evaluate
    print("Correct! Well done.")                                                   # Execute (success)
    score += 1
else:
    print(f"Wrong! The correct answer is: 7 (you said: '{answer}')")              # Execute (failure)

# ---------- Final result ----------
print("\n" + "=" * 40)
print(f"Your final score is {score} out of 3")
print("=" * 40)
