Approach:
Understood the theory behind HTTP. Utilized wireshark and firebug extention in firefox to study HTTP messages and response.Implemented the GET and POST messages to handle response.
Used socket to connect to the server.
Parsed the messages to extract links and cookie.
Created two lists visited_links and unvisited_links to verify duplicate links.
The code would traverse through the links in the respective pages check the visited lists, if it is not present there it would put it to the unvisited list and GET the page and find the FLAG. This$

Challanges:
1) To handle HTTP 302 response from the server.
2) Used Regular expression to extract cookie and session id as well as links in the html page received to use HTTP GET message to access the links.
3) Used two functions extract_links to extract links and send_links to use GET messages to access the links.
4) Opened and closed a new socket connection for every link to optimize speed and reliability.
5) We figured out that in some cases it is possible that the page can be received after some seconds and our program failed to execute beyond that, we solved this problem by adding the time module$
Testing:
1) Tested the code on linux, printed GET POST and received messages to test the code.
2) Tested different parts of code separatly before integrating them in the code.

Results:
NOTE : The output will be exactly five lines of code(The Flags) and will be produced all together and not whenever they generate. During the time of testing the average time at which the output oc$
        Also, running the Makefile would give permission to the file webcrawler and webcrawler.py.

