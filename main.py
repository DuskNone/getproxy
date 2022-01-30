import requests
import os
import sys


class GetProxy:

    def http():
        out_file = "proxyHttp.txt"
        proxies = open(out_file, 'wb')
        r1 = requests.get('https://api.openproxylist.xyz/http.txt')
        proxies.write(r1.content)
        length = []
        length.append(r1.content)
        length = length[0].splitlines()
        length1 = len(length)
        print("Completed! Successfully added {} Http proxies".format(length1))
        # os.system('pause')
        # sys.exit()

    def sock4():
        r1 = requests.get('https://api.openproxylist.xyz/socks4.txt')
        out_file = "proxySock4.txt"
        proxies = open(out_file, 'wb')
        proxies.write(r1.content)
        length = []
        length.append(r1.content)
        length = length[0].splitlines()
        length1 = len(length)
        print("Completed! Successfully added {} Sock4 proxies".format(length1))
        # os.system('pause')
        # sys.exit()

    def sock5():
        r1 = requests.get('https://api.openproxylist.xyz/socks5.txt')
        out_file = "proxySock5.txt"
        proxies = open(out_file, 'wb')
        proxies.write(r1.content)
        length = []
        length.append(r1.content)
        length = length[0].splitlines()
        length1 = len(length)
        print("Completed! Successfully added {} Sock5 proxies".format(length1))
        # os.system('pause')
        # sys.exit()


class ReadProxy():

    def http():
        print('Reading Http proxies...')
        out_file = "Proxies/proxyHttp.txt"
        # proxies = open(out_file, 'wb').readlines()
        with open(out_file) as f:
            lines = f.read().splitlines()
            # print(lines)
            return lines

    def sock4():
        print('Reading Sock4 proxies...')
        out_file = "Proxies/proxySock4.txt"
        # proxies = open(out_file, 'wb').readlines()
        with open(out_file) as f:
            lines = f.read().splitlines()
            # print(lines)
            return lines

    def sock5():
        print('Reading Sock5 proxies...')
        out_file = "Proxies/proxySock5.txt"
        # proxies = open(out_file, 'wb').readlines()
        with open(out_file) as f:
            lines = f.read().splitlines()
            # print(lines)
            return lines


if __name__ == '__main__':
    GetProxy.http()
    GetProxy.sock4()
    GetProxy.sock5()
