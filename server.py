import multiprocessing
import socket
import os


from flask import Flask
app = Flask(__name__)

@app.route("/status")
def returnProperties():
        return """{
            "hostname": \"""" + str(socket.gethostname()) + """\",
                "ip_address": \"""" + str(socket.gethostbyname(socket.gethostname())) + """\",
                    "cpus": \"""" + str(multiprocessing.cpu_count()) + """\",
                        "memory": \"""" + str(os.sysconf('SC_PAGE_SIZE')* os.sysconf('SC_PHYS_PAGES')) + """\"
                            }"""
