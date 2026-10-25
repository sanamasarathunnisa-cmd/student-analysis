"""
Student Performance Analytics System
Author : Sana Masarath Unnisa
Course : Python with AI (EWB Courses)

Run:  python main.py
"""

import os
import pandas as pd
from functions import (
    SUBJECTS, PASS_MARK, ATTENDANCE_LIMIT,
    load_data, add_student_metrics, class_statistics,
    subject_wise_analysis, department_analysis, grade_distribution,
    get_top_performers, get_failed_students,
)

# Folder where this file is saved, so the CSV is found no matter where you run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Make the printed tables look neat
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)


def print_heading(title):
    """Print a section heading."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # ---------------- Step 1 & 2: Load and inspect the data ----------------
    df = load_data(os.path.join(BASE_DIR, "students.csv"))

    print_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("Prepared by: Sana Masarath Unnisa")

    print_heading("1. DATASET OVERVIEW")
    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")
    print(f"Columns           : {list(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))
    print("\nMissing values in dataset:", int(df.isnull().sum().sum()))

    # ---------------- Step 3: Process the data ----------------
    df = add_student_metrics(df)

    print_heading("2. STUDENT-WISE RESULT (Total, Average, Grade, Result)")
    report_columns = ["Student_ID", "Name", "Department", "Total", "Average",
                      "Grade", "Result", "Attendance", "Attendance_Status"]
    print(df[report_columns].to_string(index=False))

    print(f"\nRules used -> Pass mark: {PASS_MARK} in every subject | "
          f"Minimum attendance: {ATTENDANCE_LIMIT}%")

    # ---------------- Step 4: Analysis ----------------
    stats = class_statistics(df)

    print_heading("3. CLASS PERFORMANCE SUMMARY")
    print(f"Total students       : {stats['total_students']}")
    print(f"Students passed      : {stats['passed']}")
    print(f"Students failed      : {stats['failed']}")
    print(f"Pass percentage      : {stats['pass_percentage']}%")
    print(f"Overall class average: {stats['class_average']}")
    print(f"Highest average      : {stats['highest_name']} ({stats['highest_average']})")
    print(f"Lowest average       : {stats['lowest_name']} ({stats['lowest_average']})")
    print(f"Attendance shortage  : {stats['attendance_shortage']} student(s) below {ATTENDANCE_LIMIT}%")

    print_heading("4. SUBJECT-WISE PERFORMANCE (best subject first)")
    subject_table = subject_wise_analysis(df)
    print(subject_table.to_string(index=False))
    print(f"\nBest performing subject  : {subject_table.loc[0, 'Subject']} "
          f"(average {subject_table.loc[0, 'Average']})")
    print(f"Weakest performing subject: {subject_table.loc[len(subject_table) - 1, 'Subject']} "
          f"(average {subject_table.loc[len(subject_table) - 1, 'Average']})")

    print_heading("5. TOP 5 PERFORMING STUDENTS")
    print(get_top_performers(df, 5).to_string(index=False))

    print_heading("6. GRADE DISTRIBUTION")
    print(grade_distribution(df).to_string())

    print_heading("7. DEPARTMENT-WISE PERFORMANCE")
    print(department_analysis(df).to_string())

    print_heading("8. STUDENTS WHO FAILED")
    failed = get_failed_students(df)
    if failed.empty:
        print("No student failed.")
    else:
        print(failed.to_string(index=False))

    # ---------------- Step 5: Save the final output ----------------
    df.to_csv(os.path.join(BASE_DIR, "student_results.csv"), index=False)
    print_heading("OUTPUT SAVED")
    print("Full results saved to 'student_results.csv'")


if __name__ == "__main__":
    main()