# 0x04. Loops, conditions and parsing
#### Foundations - System engineering & DevOps ― Bash
#### by Sylvain Kalache
#### Ongoing project - started 06-19-2020, must end by 06-20-2020


### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
How to create SSH keys
What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
How to use while, until and for loops
How to use if, else, elif and case condition statements
How to use the cut command
What are files and other comparison operators, and how to use them
#### The commands:
env
cut
for
while
until
if


### Requirements

#### General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
You are not allowed to use awk
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

#### 1. For Holberton School loop mandatory
Write a Bash script that displays Holberton School 10 times.
Requirement:
You must use the for loop (while and until are forbidden)
Note that:
The first line of my Bash script starts with #!/usr/bin/env bash
The second line of my Bash scripts is a comment explaining what it is doing
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 1-for_holberton_school

#### 2. While Holberton School loop mandatory
Write a Bash script that displays Holberton School 10 times.
Requirements:
You must use the while loop (for and until are forbidden)
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 2-while_holberton_school

#### 3. Until Holberton School loop mandatory
Write a Bash script that displays Holberton School 10 times.
Requirements:
You must use the until loop (for and while are forbidden)
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 3-until_holberton_school

#### 4. If 9, say Hi! mandatory
Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
Requirements:
You must use the while loop (for and until are forbidden)
You must use the if statement
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 4-if_9_say_hi

#### 5. 4 bad luck, 8 is your chance mandatory
Write a Bash script that loops from 1 to 10 and:
displays bad luck for the 4th loop iteration
displays good luck for the 8th loop iteration
displays Holberton School for the other iterations
Requirements:
You must use the while loop (for and until are forbidden)
You must use the if, elif and else statements
For the most curious:
8 in the Chinese culture
4 in the Chinese culture
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 5-4_bad_luck_8_is_your_chance

#### 6. Superstitious numbers mandatory
Write a Bash script that displays numbers from 1 to 20 and:
displays 4 and then bad luck from China for the 4th loop iteration
displays 9 and then bad luck from Japan for the 9th loop iteration
displays 17 and then bad luck from Italy for the 17th loop iteration
Requirements:
You must use the while loop (for and until are forbidden)
You must use the case statement
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 6-superstitious_numbers

#### 7. Clock mandatory
Write a Bash script that displays the time for 12 hours and 59 minutes:
display hours from 0 to 12
display minutes from 1 to 59
Requirements:
You must use the while loop (for and until are forbidden)
Note that in this example, we only display the first 70 lines using the head command.
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 7-clock

#### 8. For ls mandatory
Write a Bash script that displays:
The content of the current directory
In a list format
Where only the part of the name after the first dash is displayed (refer to the example)
Requirements:
You must use the for loop (while and until are forbidden)
Do not display hidden files
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 8-for_ls

#### 9. To file, or not to file mandatory
Write a Bash script that gives you information about the holbertonschool file.
Requirements:
You must use if and, else (case is forbidden)
Your Bash script should check if the file exists and print:
if the file exists: holbertonschool file exists
if the file does not exist: holbertonschool file does not exist
If the file exists, print:
if the file is empty: holbertonschool file is empty
if the file is not empty: holbertonschool file is not empty
if the file is a regular file: holbertonschool is a regular file
if the file is not a regular file: (nothing)
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 9-to_file_or_not_to_file

#### 10. FizzBuzz mandatory
Write a Bash script that displays numbers from 1 to 100.
Requirements:
Displays FizzBuzz when the number is a multiple of 3 and 5
Displays Fizz when the number is multiple of 3
Displays Buzz when the number is a multiple of 5
Otherwise, displays the number
In a list format
#### Repo:

GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 10-fizzbuzz

#### 11. Read and cut #advanced
help: read
Write a Bash script that displays the content of the file /etc/passwd.
Your script should only display:
username
user id
Home directory path for the user
Requirements:
You must use the while loop (for and until are forbidden)
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 100-read_and_cut


#### 12. Tell the story of passwd #advanced
Read:
IFS (internal field separator)
Understanding /etc/passwd
The file /etc/passwd has already been covered in a previous project and you should be familiar with it. Today we will make up a story based on it.
Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.
Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO
Requirements:
You must use the while loop (for and until are forbidden)
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 101-tell_the_story_of_passwd

#### 13. Let's parse Apache logs #advanced
Apache is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.

As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of Apache log access files.

Today the Customer Support department reported that a user reported that the site is being “buggy”. Not being a detailed description, you want to have a look at the Apache logs and gather data about the traffic.
Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.
Requirement:
Format: IP HTTP_CODE
in a list format
See example
You must use awk
You are not allowed to use while, for, until and cut
Download and commit the apache-access.log file along with your answers files

#### 14. Dig the data #advanced
Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.
Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.
Requirements:
The exact format must be:
OCCURENCE_NUMBER IP HTTP_CODE
In list format
Ordered from the greatest to the lowest number of occurrences
See example
You must use awk
You are not allowed to use while, for, until and cut
#### Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 103-dig_the-data