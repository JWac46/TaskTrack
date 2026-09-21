# TaskTrack

This is a program that lets you add and store tasks that you need to complete

## Current Features

-[add_task] prompts user to add a task
-[save_task] saves user input to txt file
-[load_task] loads tasks from the txt file to display
-[view_task] displays all your saved tasks

## Requirements

-Python 3

## Project Files

-`tasktrack.py` — This is the main file that runs the program
-`task.txt` — a storage system for the program
-`.gitignore` — files that need to be ignored when pushing to github

## Running the Program

Open terminal by clicking 'Terminal' in the top left and selecting 'new terminal'
OR
Open terminal with ctrl+shift+`

```to run the program type this into the terminal
py tasktrack.py
```

## Task Persistence

Tasks are initaly loaded into the program when it boots up to run. 
A task is added when the user inputs 2 to add a task and the task is loaded onto the txt file for storage

## Sample Interaction

```text
py tasktrack.py is put into the terminal

User inputs 1 to see current tasks

User inputs 2 to add a task ex: Study for quiz

User inputs 1 and sees the new task added 

User inputs 3 to exit the program
```

## Current Limitations

-The program does not allow for any sorting or level of importance for the tasks. 

## Version Control

this uses git where it stores changes locally and then uses github to upload them to the cloud

