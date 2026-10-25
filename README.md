# Student Performance Analytics System

## 1. Project Title

**Student Performance Analytics System**

| | |
|---|---|
| **Student Name** | Sana Masarath Unnisa |
| **Course** | B.Tech Computer Science Engineering (4th Year) |
| **College** | Shadan Women's College of Engineering and Technology, Hyderabad |
| **Roll Number** | _23l51A0595_ |
| **Training Program** | Python with AI – EWB Courses |

---

## 2. Objective

Teachers usually need to go through many students' marks by hand to find totals, grades, who passed and who needs help. This is slow and easy to get wrong.

This project reads student data from a CSV file and uses **Python, NumPy and Pandas** to automatically:

- calculate total and average marks for every student
- assign grades using a clear grading rule
- decide pass/fail using a clear condition
- find the highest, lowest and average performance
- analyse each subject and each department
- identify the top-performing students

The result is a clear report that can be understood without reading the code.

---

## 3. Technologies Used

| Tool | Purpose |
|---|---|
| Python 3 | Main programming language (variables, data types, loops, functions, conditions) |
| NumPy | Numerical calculations: `sum`, `mean`, `min`, `max`, `argmax`, `argmin`, `where` |
| Pandas | Loading the CSV, DataFrame operations, sorting, filtering, `groupby` |
| Git & GitHub | Version control and project submission |

---

## 4. Dataset Description

File: `students.csv` – **20 student records**, **9 columns**, no missing values.

| Column | Description |
|---|---|
| Student_ID | Unique ID (S101 – S120) |
| Name | Student name |
| Department | CSE, ECE, IT or EEE |
| Maths, Python, DBMS, Statistics, English | Subject marks out of 100 |
| Attendance | Attendance percentage |

The data is a sample dataset created for this project. It has a realistic mix of toppers, average students and students who fail or have low attendance.

---

## 5. Implementation

**Step 1 – Prepare the dataset.** Created `students.csv` with 20 students, five subjects and attendance.

**Step 2 – Read the data.** `load_data()` uses `pd.read_csv()` to load the file into a DataFrame. The program prints the number of records, columns, first 5 rows and the count of missing values.

**Step 3 – Process the data.** `add_student_metrics()` loops through every student (`for ... in df.iterrows()`). For each student it converts the marks to a NumPy array and calls:

- `calculate_total()` → `np.sum()`
- `calculate_average()` → `np.mean()`
- `check_result()` → `np.min()` to find the lowest subject mark
- `assign_grade()` → grading rule using `if / elif / else`

The new columns `Total`, `Average`, `Result`, `Grade` are added to the DataFrame. `np.where()` is used to create the `Attendance_Status` column.

**Step 4 – Perform the analysis.**

- `class_statistics()` → pass/fail counts, class average, highest and lowest using `np.argmax()` / `np.argmin()`
- `subject_wise_analysis()` → average, highest, lowest and pass count for each subject
- `department_analysis()` → Pandas `groupby()` for department-wise results
- `grade_distribution()` → number of students in each grade
- `get_top_performers()` → students sorted by average and ranked
- `get_failed_students()` → failed students and the subjects they failed in

**Step 5 – Final output.** `main.py` prints every result under a clear heading and saves the complete table to `student_results.csv`.

### Rules used

**Grading rule (based on average marks)**

| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| 40 – 49 | E |
| Below 40 | F |

**Pass/Fail rule:** a student **passes** only if they score **40 or more in every subject**. A student who fails any subject gets grade **F**.

**Attendance rule:** attendance below **75%** is marked as `Shortage`.

---

## 6. Key Features

- Loads and organises data with a Pandas DataFrame
- Reusable functions kept in `functions.py`
- Loops used to process each student
- NumPy used for all numerical calculations
- Total, average, grade and pass/fail for each student
- Highest, lowest and class average
- Subject-wise analysis with best and weakest subject
- Department-wise analysis
- Grade distribution
- Top 5 performers ranking
- Failed students list with the subjects failed
- Attendance shortage detection
- Results exported to `student_results.csv`

---

## 7. Output / Screenshots
![alt text](image-1.png)
![alt text](image.png)
![![![![alt text](image-5.png)](image-4.png)](image-3.png)](image-2.png)
Sample output from the program:

```
CLASS PERFORMANCE SUMMARY
Total students       : 20
Students passed      : 17
Students failed      : 3
Pass percentage      : 85.0%
Overall class average: 70.18
Highest average      : Ayesha Fatima (94.2)
Lowest average       : Vikram Chowdary (40.6)
Attendance shortage  : 6 student(s) below 75%

SUBJECT-WISE PERFORMANCE (best subject first)
   Subject  Average  Highest  Lowest  Students_Passed
   English    73.15       92      48               20
    Python    71.30       98      38               19
      DBMS    68.90       94      36               19
     Maths    68.80       95      33               18
Statistics    68.75       96      38               19

TOP 5 PERFORMING STUDENTS
 Rank Student_ID             Name Department  Total  Average Grade
    1       S102    Ayesha Fatima        CSE    471     94.2    A+
    2       S108 Lakshmi Prasanna         IT    453     90.6    A+
    3       S117     Shreya Patel        CSE    450     90.0    A+
    4       S101      Aarav Reddy        CSE    433     86.6     A
    5       S110     Zainab Begum        CSE    430     86.0     A

GRADE DISTRIBUTION
A+ 3 | A 4 | B 4 | C 4 | D 2 | E 0 | F 3

STUDENTS WHO FAILED
Student_ID            Name Department  Average         Failed_In
      S105     Rahul Verma        EEE     43.6 Maths, Statistics
      S111     Rohit Kumar        ECE     43.4            Python
      S120 Vikram Chowdary        EEE     40.6       Maths, DBMS
```

---

## 8. Final Outcome

The project successfully reads the student dataset and produces a complete performance report. From the 20 records it found:

- **17 students passed and 3 failed** (pass percentage 85%)
- the **class average is 70.18**
- **Ayesha Fatima** has the highest average (94.2) and **Vikram Chowdary** the lowest (40.6)
- **English** is the best-performing subject (average 73.15) and **Statistics** the weakest (68.75)
- **CSE** has the highest department average (85.17) and **EEE** the lowest (49.90)
- 6 students have attendance below 75%

All the required features of the assignment are implemented, and the output can be understood without opening the code.

---

## 9. Challenges & Learning

| Challenge | How it was solved |
|---|---|
| A student could have a good average but still fail one subject, which made the grade confusing | Pass/fail is decided by the lowest subject mark (`np.min`), and any student who fails a subject gets grade F |
| Deciding where to use a loop and where to use Pandas/NumPy directly | Used a loop for per-student processing and NumPy/Pandas for whole-column calculations |
| Keeping the code readable as it grew | Moved all calculations into reusable functions in `functions.py` and kept `main.py` only for printing the report |
| Changing rules (pass mark, subjects, attendance limit) | Stored them as constants at the top of `functions.py` so they can be changed in one place |

**What I learned:** working with DataFrames, using NumPy functions such as `sum`, `mean`, `argmax` and `where`, writing reusable functions, using `groupby` for summaries, and organising a project so it can be pushed to GitHub and understood by others.

---

## 10. GitHub Repository

**Link:** _<(https://github.com/sanamasarathunnisa-cmd/student-analysis/)>_

### Project structure

```
student-performance-analytics/
├── main.py              # runs the project and prints the analysis
├── functions.py         # reusable calculation / processing functions
├── students.csv         # student dataset (20 records)
├── student_results.csv  # output generated by main.py
└── README.md            # project documentation
```

### How to run

```bash
pip install pandas numpy
python main.py
```
