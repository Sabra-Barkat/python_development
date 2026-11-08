# Project 4 (Bonus): General Knowledge Quiz
# Extras: .casefold(), multiple valid answers, f-string alignment, percentage + message

print("=" * 40)
print("   General Knowledge Quiz - Bonus Edition")
print("=" * 40)

score = 0
total = 3

# ---------- Question 1 ----------
answer = input("\nQ1. What is the capital of France? ")   # Ask & Capture
answer = answer.strip().casefold()                         # Sanitize
if answer in ("paris", "paris, france"):                   # Evaluate (multiple valid answers)
    print("Correct!")                                      # Execute (success)
    score += 1
else:
    print("Wrong! The correct answer is: paris")           # Execute (failure)

# ---------- Question 2 ----------
answer = input("\nQ2. Which planet is known as the Red Planet? ")
answer = answer.strip().casefold()
if answer in ("mars", "planet mars"):
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: mars")

# ---------- Question 3 ----------
answer = input("\nQ3. How many continents are there on Earth? ")
answer = answer.strip().casefold()
if answer in ("7", "seven"):
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: 7 (seven)")

# ---------- Final result ----------
percentage = score / total * 100
print("\n" + "=" * 40)
print(f"Your final score is {score:>2} out of {total}")
print(f"Percentage: {percentage:.0f}%")
if score == 3:
    print("Outstanding! Perfect score!")
elif score == 2:
    print("Great job! Almost perfect.")
elif score == 1:
    print("Good try. Keep practicing!")
else:
    print("Don't give up. Try again!")
print("=" * 40)
