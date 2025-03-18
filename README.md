## Proofpoint-test

## Structure

- **environment/**: Virtual environment with the necessary dependencies.
- **taskB/**: Module for Task B.
    - `back.py`: Contains the code.
    - `inputFile.csv`: An example CSV used to test the code.
- **taskC/**: Module for Task C.
    - `back.py`: Contains the code.
    - `inputFile.txt`: An example TXT used to test the code.
- `front.py`: Interface to interact with the two modules.
- `requirements.txt`: Dependencies of the project.
- `taskA.txt`: Answer for Task A.
- `to-do.txt`: File with the description of the three tasks.

Requires Python and pip installed to create the environment work.

## Instructions

1. **Create the virtual environment**:
     ```bash
     python -m venv environment
     ```
2. **Activate the virtual environment**:
     ```bash
     environment/Scripts/Activate
     ```
3. **Install the dependencies**:
     ```bash
     pip install -r requirements.txt
     ```
4. **Once the installation has finished, execute the file**:
     ```bash
     python front.py
     ```
**Outputs**:
    - **Task B**: `booklist-by-{filter}.csv` (Headers: Title, Author, Year).
    - **Task C**: `wordCounter.csv` (Headers: Word, Counter).