from flask import Flask
import os
from datetime import datetime, timezone, timedelta
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Abdul Rahim Shaik"
    username = os.getenv("USER") or "codespace"  # Alternative to os.getlogin()
    
    ist_offset = timedelta(hours=5, minutes=30)
    server_time = datetime.now(timezone.utc) + ist_offset
    formatted_time = server_time.strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1 | head -n 10')
    
    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time in IST: {formatted_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
