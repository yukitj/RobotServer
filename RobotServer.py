import socketserver, time, json

rbts_state = {}
state_req = [b'cart_pos\r', b'jnt_pos\r', b'jnt_vel\r', b'jnt_trq\r', b'alarm_info\r', b'state\r', b'robot_running_state\r']

class RokaeRbtHandler(socketserver.BaseRequestHandler):

    def handle(self):
        key = self.client_address[0]
        l = len(state_req)
        r = [None] * l
        conn = True
        if key == '192.168.2.100':
            a = self.request.recv(1024)
            if a == b'get_robots_info':
                self.request.sendall(json.dumps(rbts_state).encode('utf-8'))
            else:
                self.request.sendall(b'{}')
            return
        while conn:
            time.sleep(0.1)
            for i in range(l):   #取state_req指令队列长度
                try:
                    self.request.sendall(state_req[i])  #逐条发送
                    a = self.request.recv(1024)   #recv message
                except ConnectionError:
                    conn = False
                    break
                if not a:
                    conn = False
                    break
                r[i] = a.strip().decode('utf-8')
            if conn:
                rbts_state[key] = r
            else:
                rbts_state.pop(key)


if __name__ == "__main__":

    HOST, PORT = "192.168.2.100", 9999

    with socketserver.ThreadingTCPServer((HOST, PORT), RokaeRbtHandler) as server:
        server.serve_forever()
