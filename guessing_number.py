print("===== Number Guessing Game =====")
print(" think of a number between 1 and 20.")
secret_number = 12  
guess = int(input("Enter your guess: "))
if guess == secret_number:
    print("🎉 Congratulations! You guessed it right.")
elif guess > secret_number:
    print("Too high! The number was", secret_number)
else:
    print("Too low! The number was", secret_number)



