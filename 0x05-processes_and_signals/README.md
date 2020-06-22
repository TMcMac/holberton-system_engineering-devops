# 0x05. Processes and signals
#### Foundations - System engineering & DevOps ― Bash   
#### by Sylvain Kalache
#### Ongoing project - started 06-22-2020, must end by 06-23-2020

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

### Tasks

#### 0. What is my PID mandatory
Write a Bash script that displays its own PID.
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 0-what-is-my-pid

#### 1. List your processes mandatory
Write a Bash script that displays a list of currently running processes.
Requirements:
Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 1-list_your_processes

#### 2. Show your Bash PID mandatory
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
Requirements:
You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 2-show_your_bash_pid

#### 3. Show your Bash PID made easy mandatory
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
Requirements:
You cannot use ps
Here we can see that:
For the first iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4555
For the second iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4557
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 3-show_your_bash_pid_made_easy

#### 4. To infinity and beyond mandatory
Write a Bash script that displays To infinity and beyond indefinitely.
Requirements:
In between each iteration of the loop, add a sleep 2
Note that I ctrl+c (killed) the Bash script in the example.
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 4-to_infinity_and_beyond

#### 5. Kill me now mandatory
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that kills 4-to_infinity_and_beyond process.
Requirements:
You must use kill
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 5-kill_me_now

#### 6. Kill me now made easy mandatory
Write a Bash script that kills 4-to_infinity_and_beyond process.
Requirements:
You cannot use kill or killall
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 6-kill_me_now_made_easy

#### 7. Highlander mandatory
Write a Bash script that displays:
To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 7-highlander

#### 8. Beheaded process mandatory
Write a Bash script that kills the process 7-highlander.
Repo:
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 8-beheaded_process