# Backdoor
A backdoor program that injects itself via the web into the user's computer and hands the target computer's directory control to the server.

## Instructions

1. Open the <code>client.py</code> file and spot the <code>HOST</code> variable declaration in the beginning.
2. Enter the server system's name / IP address within the empty quotes and save the program.
3. Test the server and client programs in two separate Anaconda Prompt / Terminal / Command Prompt windows.<br />If everything is fine, you will notice a set of information of the client system (in this case, your own system) appear in the server prompt indicating you are good to go.
4. Type <code>help</code> and hit enter to see a list of commands to execute.
5. Type <code>exit</code> and hit enter to exit the program.

### To use on different systems:
1. Make sure you have followed the above steps.
2. Rename the <code>client.py</code> to some tempting name such as <code>ms_service_pack_v3.1.8x64.py</code>.
3. Convert the above <code>.py</code> file into an executable (<code>.exe</code>) by running the <p><center><code>pyinstaller --onefile ms_service_pack_v3.1.8x64.py</code></center></p> command in your Anaconda Prompt / Terminal / Command Prompt.
4. Once completed, add the <code>build</code> and <code>dist</code> folders as well as the <code>.spec</code> file to zip / rar.
5. Transfer this <code>.zip</code> / <code>.rar</code> file to the other system. (Or better, make the target system download the file from a website like the one listed in the project - <code>index.html</code>.)
6. On your system (server), go to Control Panel -> System and Security -> Windows Defender Firewall.
7. On the left panel, click Turn Windows Defender Firewall on or off.
8. Under 'Public Networks', click the 'Turn off Windows Defender Firewall' option and click OK.
9. Open the Anaconda prompt / Terminal / Command Prompt and run the 'server.py' file.
10. On the other system (client), navigate to the <code>dist</code> folder and execute the <code>.exe</code> file. (Make sure the server on the other system is running as you do this.)

This should establish a connection between the client and the server and hand the client system's directory control over to the server.
Type <code>help</code> to see the list of available commands and play around with them to manipulate the client system's files.
