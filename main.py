print("🌟 SMART HABIT TRACKER WITH REWARD SYSTEM 🌟")
print("-------------------------------------------")

# Step 1: Take habits
habits = []
a=int(input())
for i in range(a):
    habit = input()
    habits.append(habit)

points = 0

# Step 2: Loop through days
days = int(input())

for d in range(1, days + 1):
    print(f"\n📅 Day {d}")

    for h in habits:
        status = input(f"Did you complete '{h}' today? (yes/no): ").lower()

        if status == "yes":
            points += 10
            print("✔ Good job! +10 points")
        else:
            points -= 5
            print("✘ Try harder! -5 points")

    # Daily status
    print(f"✨ Total Points so far: {points}")

    if points < 0:
        print("⚠ Warning: Your habits are slipping!")
    elif points >= 50:
        print("🏆 Congratulations! You reached LEVEL UP!")
        print("You are building strong habits!")
        break

# Step 3: Final Summary
print("\n----------------------------")
print("📊 FINAL HABIT REPORT")
print(f"Total Points Earned: {points}")

if points >= 50:
    print("🎉 Excellent Consistency! Keep it up!")
elif points >= 20:
    print("👍 Good effort! Improve more!")
else:
    print("😕 Needs improvement. You can do better!")
