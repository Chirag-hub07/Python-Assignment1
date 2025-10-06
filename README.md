# 🥗 Calorie Tracking Console App

*A simple and interactive Python-based console application to help you track your daily meals and calorie intake.*

---

## 📖 Overview

The **Calorie Tracking Console App** allows users to log their daily meals and monitor their calorie intake compared to a personal calorie limit. It provides an easy-to-read summary of meals, total calories, and average calories per meal, along with guidance messages to help maintain dietary goals.

Additionally, users can choose to save their daily summary to a log file for tracking progress over time.

---

## ✨ Features

* ✅ User-friendly console interface.
* ✅ Log multiple meals with calorie values.
* ✅ Calculate **total** and **average** calories.
* ✅ Compare intake with a **custom daily calorie limit**.
* ✅ Motivational feedback based on calorie balance.
* ✅ Option to save a detailed summary report with a timestamp.

---

## 📂 File Generated

When the user chooses to save the report, the app generates a file named:

```
calorie_log.txt
```

This file contains:

* Date & time of the report
* Meal-wise calorie breakdown
* Total and average calories
* User’s daily calorie limit
* Personalized feedback

---

## 🖥️ Demo (Console Preview)

```text
=========================================
 Welcome to Calorie Tracking Console App
=========================================

Hi! Let's turn your meals into insights.

- Log every bite from morning till night.
- Compare with your daily calorie goal.
- Stay on track and crush your health targets.

Your path to smarter eating starts now!
=========================================

Please enter the number of meals you want to track: 3  

Enter meal 1 name: Breakfast  
Enter calories intake for Breakfast: 400  
Enter meal 2 name: Lunch  
Enter calories intake for Lunch: 650  
Enter meal 3 name: Dinner  
Enter calories intake for Dinner: 500  

Enter your Daily Calorie Limit: 1600
```

**Sample Output:**

```text
==============================
      CALORIE SUMMARY
==============================
Meal Name           Calories
------------------------------
Breakfast              400 kcal
Lunch                  650 kcal
Dinner                 500 kcal
------------------------------
Total:                1550 kcal
Average:               516.67 kcal
==============================

Great balance! Your calories are in range.  
Keep fueling your body the smart way.
```

---

## ⚙️ How to Run

1. Clone or download the repository.
2. Ensure you have **Python 3.x** installed.
3. Run the program in your terminal or IDE:

```bash
python calorie_tracker.py
```

---

Would you like me to also include **ASCII art preview** (like the flame + banner) inside the README so it looks cooler w
