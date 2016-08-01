The following apps were tested in both the app and the mobile site version to check for the leaked PII.

1) Badoo
2) Ebay
3) Match Dating
4) CBS Sports
5) Tumblr
6) Kayak
7) NCAA sports

PROCEDURE:
The generated the dump files were renamed and a log file was created using dump2bro.
The log files were renamed and using vi editor i searched the files for information and then wrote a python script to get the count of the data leaked.

OBSERVATION:
The log files are present in the /home/mohana/bro-logs/project6
The dump files are present renamed in the /home/mohana/ALLDUMPS
All the log files that are given with the suffix "s" stand for the https version except fot files the badooapplicationhttp/https.log, badoobrowserhttp/https.log, cbssportsapplicationhttp/https.log$
The main aim of the project was to find important information that was leaked. The log files that were generated parsed using a own created python code.
The most surprising for me was when I checked badoo app, it leaked most of my phone information like serial number, device name, advid, model, device color, battery and memory. I believe that this$
All the apps were tested through Safari and two apps (NCAA Sports and Tumblr)  were tested through safari and Chrome also.

HOW TO RUN THE CODE:
To run the code i have written a bash script.First run the Makefile to give permissions to the file Recon.It can be run using the following command

./Recon [Filename]

CHALLENGES:
The main challenge was to find the information and the format in which it is actually shown in the log file.

OUTPUT(LOOKS LIKE THIS):
No of unique addresses contacted = 0
emailid_leaked =  0
Build_version leaked =  0
Device_name leaked =  0
Battery_level leaked =  0
timezone leaked =  0
Carrier_information leaked =  0
Advertising_ID leaked =  0
Device_info leaked =  0
OS_Version leaked =  0
Serial_Number of the phone leaked =  0
IMEI_Number of the phone leaked =  0
USERNAME of the ACCOUNT inplain text =  0
password of the account in plain text =  0
MAC_address of the phone is leaked =  0
Model of the phone is leaked =  0

