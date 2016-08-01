Approach:
Approach was to prepare a code to accept messages similar to the ccis server and extract operators and numbers from the messages, operate accordingly and provide output.
Implement socket around the code to connect to the server and accept paramters to connect to the ccis machines and respond to the messages by the server.
Implemented a bash script to execute code according to the parameters provided to the script.
Created a makefile to provide permissions to the file and execute. 



Challenges:
1) to accept messages
Solution: Python Regular Expressions.
2) to separate operators from Numbers:
Solution: match function
3) to extract numbers from Expression:
Solution: Split function:
4) Bash script to accept different types of arguements and provide error message with invalid 
Solutions: Used Nested If then else to handle input.
5) Connect to the machine via ssl
 using import ssl and used wrap_socket funtions without using certificates.


Testing:
Tested on VMware: created a simple server to send solutions of Expressions provided as input to the client.
Tested on CCIS server.
Printed intermidiate output to debug the code.
