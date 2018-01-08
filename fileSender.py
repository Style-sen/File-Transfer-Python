import time
import os
import socket
import logging
import argparse
PORT = 10000
HOST = '192.168.12.161'

print('\033[46m\033[34m\033[1mBienvenido al File Sender v.0.02 hecho en Python. Este programa permite enviar archivos a traves de tu maquina\033[0m')

class SendFileLine():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST,PORT))
        self.socket.listen(1)
        self.fname = ""

    def socket_accept(self):
        self.conn, addr = self.socket.accept()
        
    def send_file_by_line(self):
        fileToSend = open(self.fname, 'rb')
        while True:
            time.sleep(0.1)
            data = fileToSend.readline()
            print(data)
            if data:
                self.conn.send(data)
            else:
                break
        fileToSend.close()




def main():
    # get input files
    parser = argparse.ArgumentParser(description="Send txt files.")
    parser.add_argument('txt_files', metavar = 'txt_list', help='Txt_file.')
    args = parser.parse_args()

    sfl = SendFileLine()
    sfl.fname = args.txt_files
    sfl.socket_accept()
    while True:
        sfl.send_file_by_line()

    
if __name__ == '__main__':

    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                  "[%(module)s:%(lineno)d] %(message)s")
    # setup console logging
    log.setLevel(logging.WARN)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)

    ch.setFormatter(formatter)
    log.addHandler(ch)

    main()
