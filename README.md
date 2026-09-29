# Student Record Manager

A command-line Python app for adding, viewing, and deleting student records. Data is validated on input and saved to a JSON file.

## Features

- **Add a student:** roll number, name, age, gender, and class
- **View** all students, or only the students in one class
- **Delete** a student by roll number
- **Input validation**
  - Roll number must be a whole number and must not already exist
  - Age must be a whole number from 1 to 30
  - Invalid input is rejected and the user is asked again
- **Saved automatically:** records are loaded on start and saved after every add or delete
- **Corrupted-file protection:** a damaged data file is backed up, not overwritten
- **Tests** with `pytest`

## Project structure

- `main.py`: the menu, user input, validation, and add/view/delete actions
- `models.py`: the `Student` dataclass and its conversion to and from a dictionary
- `storage.py`: loading and saving `students.json`, including corrupted-file backup
- `test_models.py`: tests for converting a `Student` to and from a dictionary
- `students.json`: the data file. It is created when the app runs and is not committed to Git

## Setup and run

Requires **Python 3.12+**.

```bash
git clone https://github.com/AnshGIll/student-record-manager.git
cd student-record-manager

python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
python main.py
```

## Running tests

```bash
pytest
```

The tests check that:
- `to_dict()` turns a `Student` into a dictionary with every field correct
- `from_dict()` rebuilds a `Student` with every field in the right place

Each field uses a different value, so if two fields ever get swapped, the tests fail.

## Engineering notes

### 1. The bug this project fixed

The first version had two real bugs:

1. **Wrong argument order.** `main.py` passed values to `Student(...)` in a different order than the class expected. Python accepted it, so names, ages, and classes were silently stored in the wrong fields.
2. **Missing `to_dict()`.** Saving called a method that didn't exist, so the first save crashed with `AttributeError` and nothing was ever written to the file.

**The fix:** the argument order was corrected, the missing `to_dict()` was added, `Student` became a typed dataclass, and tests were added that catch a field swap in well under a second.

**What the tests don't cover:** they protect `to_dict()` and `from_dict()`, not the `Student(...)` call in `main.py`. Using keyword arguments there is listed as a future improvement.

### 2. Corrupted data file

If `students.json` is damaged, the app does **not** crash and does **not** overwrite it:

- **Broken data** (invalid JSON, a missing field, or the wrong data type): the file is renamed to a timestamped backup (`student_corrupted_<date>_<time>.json`) and the app starts with an empty list. The old records can still be recovered from the backup.
- **File can't be read** (for example, no permission): the app shows the error and starts empty, but doesn't rename anything, because the file itself may be fine.

Backup files are excluded from Git in `.gitignore`.

## Known limitations

- The student list is a **global variable** in `main.py`, which makes the validation functions hard to test.
- **Name, gender, and class are not validated.** Empty text is accepted.
- **"Student added successfully!" is shown even if saving fails.**
- The data file path depends on **which folder you run the app from**.

## Future improvements

- Validate name, gender, and class
- Replace the global list with a small service class
- Report save failures to the user
- Store the data file in a fixed location
- Use keyword arguments when creating `Student` objects
- Add tests for storage, corrupted-file recovery, duplicate roll numbers, and invalid ages