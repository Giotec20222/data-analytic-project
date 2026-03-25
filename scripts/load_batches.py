
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Clear the students table to avoid duplicate key errors
cur.execute("DELETE FROM students;")

with open("data/student_health_data.csv", "r") as file:
    reader = csv.DictReader(file)
    row_count = 0
    for row in reader:
        cur.execute(
            """
            INSERT INTO students (
                student_id, age, gender,
                heart_rate, blood_pressure_systolic, blood_pressure_diastolic,
                stress_level_biosensor, stress_level_self_report,
                physical_activity, sleep_quality, mood,
                study_hours, project_hours, health_risk_level, family_members
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["Student_ID"],
                row["Age"],
                row["Gender"],
                row["Heart_Rate"],
                row["Blood_Pressure_Systolic"],
                row["Blood_Pressure_Diastolic"],
                row["Stress_Level_Biosensor"],
                row["Stress_Level_Self_Report"],
                row["Physical_Activity"],
                row["Sleep_Quality"],
                row["Mood"],
                row["Study_Hours"],
                row["Project_Hours"],
                row["Health_Risk_Level"],
                row["Family_members"]
            )
        )
        row_count += 1
        if row_count % 100 == 0:
            print(f"Inserted {row_count} rows...")

conn.commit()
print(f"Successfully inserted {row_count} rows from CSV.")
cur.close()
conn.close()