# Time-Management-System

# ⏰ Time Management Tracker

A simple Python project that helps users track how they spend their time in a day. The program collects the number of hours spent on different activities, displays the data in a table, and visualizes it using a pie chart.

---

## 📌 Features

- Accepts user input for daily activities:
  - 😴 Sleep
  - 💼 Work
  - 📱 Phone
  - 📚 Study
- Calculates:
  - Total hours used
  - Active hours
  - Remaining free time
- Checks whether the user is getting enough sleep.
- Displays activity data in a Pandas DataFrame.
- Generates a pie chart using Matplotlib.

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib

---

## 📂 Project Structure

```
Time-Management-Tracker/
│
├── time_management.py
├── README.md
└── screenshot.png
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Time-Management-Tracker.git
```

### 2. Open the project folder

```bash
cd Time-Management-Tracker
```

### 3. Install required libraries

```bash
pip install pandas matplotlib
```

### 4. Run the program

```bash
python time_management.py
```

---

## 💻 Sample Input

```
Sleep: 8
Work: 6
Phone: 4
Study: 5
```

---

## 📊 Sample Output

```
Total time used: 23
Active time: 15

Activity   Hours
Sleep      8
Work       6
Phone      4
Study      5

You are having enough sleep.
You have 1 hour(s) for free time.
```

---

## 📷 Screenshot

Add your project screenshot here.

Example:

![Project Screenshot](screenshot.png)

---

## 📈 Future Improvements

- Add more daily activities
- Save data to CSV
- Weekly and monthly reports
- Bar chart visualization
- GUI using Tkinter
- Data validation for incorrect inputs

---
