
import subprocess
import sys
import os

# Main project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Execution order
programs = [
    "cleaning.py",
    "analysis.py",
    "visualization.py",
    "sql.py",
    "excel_report.py"
]

print("\n" + "=" * 60)
print(" SOLAR ENERGY INTELLIGENCE & PREDICTIVE GENERATION")
print("=" * 60)

for i, program in enumerate(programs, start=1):

    file_path = os.path.join(SRC_DIR, program)

    print(f"\nSTEP {i}/{len(programs)}: Running {program}")
    print("-" * 60)

    if not os.path.isfile(file_path):
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, file_path],
        cwd=BASE_DIR
    )

    if result.returncode != 0:
        print(f"\nFAILED: {program}")
        print("Execution stopped due to an error.")
        sys.exit(result.returncode)

    print(f"COMPLETED: {program}")

print("\n" + "=" * 60)
print(" ALL 5 PROGRAMS COMPLETED SUCCESSFULLY!")
print("=" * 60)
