"""Infrastructure connector"""
def connect(host, user="root", key=None):
    return {"host": host, "user": user, "connected": True}
def run(host_conn, cmd):
    return {"stdout": "executed: " + cmd, "rc": 0}
def deploy(host_conn, source, dest):
    return {"status": "deployed"}
