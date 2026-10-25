"""
functions.py
Reusable functions for the Student Performance Analytics System.
Author: Sana Masarath Unnisa
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# Project settings (easy to change in one place)
# ---------------------------------------------------------------
SUBJECTS = ["Maths", "Python", "DBMS", "Statistics", "English"]
PASS_MARK = 40            # minimum marks needed in EVERY subject
ATTENDANCE_LIMIT = 75     # minimum attendance percentage


# ---------------------------------------------------------------
# 1. Loading data
# ---------------------------------------------------------------
def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


# ---------------------------------------------------------------
# 2. Single-student calculations (used inside a loop)
# ---------------------------------------------------------------
def calculate_total(marks):
    """Return total marks using NumPy."""
    return int(np.sum(marks))


def calculate_average(marks):
    """Return average marks (rounded to 2 decimals) using NumPy."""
    return round(float(np.mean(marks)), 2)


def assign_grade(average, has_failed):
    """
    Grading rule (based on average marks):
        90 and above  -> A+
        80 to 89      -> A
        70 to 79      -> B
        60 to 69      -> C
        50 to 59      -> D
        40 to 49      -> E
        below 40      -> F
    A student who fails in any subject always gets grade F.
    """
    if has_failed:
        return "F"
    elif average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def check_result(marks):
    """
    Pass/Fail rule:
    A student PASSES only if marks in every subject are >= PASS_MARK.
    """
    if np.min(marks) >= PASS_MARK:
        return "Pass"
    return "Fail"


# ---------------------------------------------------------------
# 3. Process the whole DataFrame (loop over every student)
# ---------------------------------------------------------------
def add_student_metrics(df):
    """
    Loop through each student and add:
    Total, Average, Result, Grade and Attendance_Status columns.
    """
    totals = []
    averages = []
    results = []
    grades = []

    for index, row in df.iterrows():
        marks = row[SUBJECTS].to_numpy(dtype=int)   # this student's marks as a NumPy array

        total = calculate_total(marks)
        average = calculate_average(marks)
        result = check_result(marks)
        grade = assign_grade(average, result == "Fail")

        totals.append(total)
        averages.append(average)
        results.append(result)
        grades.append(grade)

    df = df.copy()
    df["Total"] = totals
    df["Average"] = averages
    df["Result"] = results
    df["Grade"] = grades

    # NumPy where(): vectorised if-else for attendance
    df["Attendance_Status"] = np.where(df["Attendance"] >= ATTENDANCE_LIMIT,
                                       "OK", "Shortage")
    return df


# ---------------------------------------------------------------
# 4. Class-level analysis
# ---------------------------------------------------------------
def class_statistics(df):
    """Return highest, lowest and overall class performance as a dictionary."""
    averages = df["Average"].to_numpy()

    top_index = int(np.argmax(averages))      # position of highest average
    low_index = int(np.argmin(averages))      # position of lowest average

    stats = {
        "total_students": len(df),
        "passed": int((df["Result"] == "Pass").sum()),
        "failed": int((df["Result"] == "Fail").sum()),
        "pass_percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_name": df.loc[top_index, "Name"],
        "highest_average": float(averages[top_index]),
        "lowest_name": df.loc[low_index, "Name"],
        "lowest_average": float(averages[low_index]),
        "attendance_shortage": int((df["Attendance_Status"] == "Shortage").sum()),
    }
    return stats


def subject_wise_analysis(df):
    """Return a table with average, highest, lowest and pass count for each subject."""
    rows = []
    for subject in SUBJECTS:
        marks = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Students_Passed": int(np.sum(marks >= PASS_MARK)),
        })
    return pd.DataFrame(rows).sort_values("Average", ascending=False).reset_index(drop=True)


def department_analysis(df):
    """Average marks and pass count for each department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.sort_values("Avg_Marks", ascending=False)


def grade_distribution(df):
    """Count of students in each grade (in a fixed order)."""
    order = ["A+", "A", "B", "C", "D", "E", "F"]
    counts = df["Grade"].value_counts()
    return counts.reindex(order, fill_value=0)


def get_top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n).copy()
    top.insert(0, "Rank", range(1, len(top) + 1))
    return top[["Rank", "Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def get_failed_students(df):
    """Return students who failed, along with the subjects they failed in."""
    failed = df[df["Result"] == "Fail"].copy()
    failed_subjects = []
    for index, row in failed.iterrows():
        subjects_failed = [s for s in SUBJECTS if row[s] < PASS_MARK]
        failed_subjects.append(", ".join(subjects_failed))
    failed["Failed_In"] = failed_subjects
    return failed[["Student_ID", "Name", "Department", "Average", "Failed_In"]]
