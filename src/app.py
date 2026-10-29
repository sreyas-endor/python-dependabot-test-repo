import hashlib
import pickle
import subprocess

import yaml
from flask import Flask, request

app = Flask(__name__)

# Fake credentials for the PR-dismissal bug bash. None of these are real.
DB_PASSWORD = "Zq7!mR2vXk9Lp4@Wt8sNb3Y"
GENERIC_API_KEY = "api_key_9f3b7c1e5d8a2f4b6c0e9d7a3b1f5c8e"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidWdiYXNoIiwibmFtZSI6IlBSIGRpc21pc3MgdGVzdCIsImlhdCI6MTc5MzIwMDAwMH0.Qx3v9Lp2Rt5Wz1Yb7Nc4DaKe3Vs6Uj0FgThMk8sPq1"


@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr")))


@app.route("/load", methods=["POST"])
def load():
    return str(yaml.load(request.data))


@app.route("/restore", methods=["POST"])
def restore():
    return str(pickle.loads(request.data))


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
