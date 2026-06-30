import random
sentences = [
    "Python is easy to learn.",
    "Programming improves problem solving skills.",
    "Embedded systems are everywhere.",
    "Practice makes a programmer perfect.",
    "STM32 microcontrollers are powerful.",
    "Typing speed increases with practice.",
    "Always write clean and readable code."
]
def calculate_accuracy(original, typed):
    if not typed:
        return 0.0
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    max_len = max(len(original), len(typed))
    return (correct / max_len) * 100

while True:
    sentence = random.choice(sentences)
    print("\n==============================")
    print("      SPEED TYPING TEST")
    print("==============================")
    print("\nType the following sentence:\n")
    print(sentence)
    input("\nPress Enter to Start...")
    typed = input("\nType here:\n")
    accuracy = calculate_accuracy(sentence, typed)
    print("\n========== RESULT ==========")
    print(f"Accuracy : {accuracy:.2f}%")
    if typed == sentence:
        print("Status   : Perfect! ")
    elif accuracy >= 90:
        print("Status   : Excellent ")
    elif accuracy >= 75:
        print("Status   : Good ")
    elif accuracy >= 50:
        print("Status   : Fair ")
    else:
        print("Status   : Needs Practice ")
        
    again = input("\nPlay Again? (y/n): ").lower()
    if again != "y":  
        break
print("\nThanks for playing!")
