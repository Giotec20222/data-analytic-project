CREATE TABLE IF NOT EXISTS students (
    student_id              INTEGER PRIMARY KEY,
    age                     NUMERIC,
    gender                  VARCHAR(10),
    heart_rate              NUMERIC,
    blood_pressure_systolic NUMERIC,
    blood_pressure_diastolic NUMERIC,
    stress_level_biosensor  NUMERIC,
    stress_level_self_report NUMERIC,
    physical_activity       VARCHAR(20),
    sleep_quality           VARCHAR(20),
    mood                    VARCHAR(20),
    study_hours             NUMERIC,
    project_hours           NUMERIC,
    health_risk_level       VARCHAR(20),
    family_members          INTEGER
);
