from flask import Flask, render_template, jsonify
import socket
import threading

app = Flask(__name__)

# Global variable to store the latest traffic data
data_store = {"car_count": 0, "status": "Initializing"}

def socket_listener():
    """Background thread to listen for data from the Vision script"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 5006)) # Different port for the dashboard
    while True:
        data, _ = sock.recvfrom(1024)
        count = int(data.decode())
        data_store["car_count"] = count
        data_store["status"] = "Heavy Traffic" if count > 5 else "Fluid Traffic"

@app.route('/')
def index():
    return """
    <html>
        <head><title>Traffic Control Center</title></head>
        <body style="font-family: sans-serif; text-align: center; background: #f0f0f0;">
            <h1>🚦 Traffic Intelligence Dashboard</h1>
            <div style="font-size: 2em; margin: 20px; padding: 20px; background: white; border-radius: 10px; display: inline-block;">
                <p>Live Car Count: <span id="count">0</span></p>
                <p>System Status: <b id="status">Loading...</b></p>
            </div>
            <script>
                setInterval(() => {
                    fetch('/api/data').then(r => r.json()).then(data => {
                        document.getElementById('count').innerText = data.car_count;
                        document.getElementById('status').innerText = data.status;
                        document.getElementById('status').style.color = data.car_count > 5 ? 'red' : 'green';
                    });
                }, 1000);
            </script>
        </body>
    </html>
    """

@app.route('/api/data')
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    # Start the background listener
    threading.Thread(target=socket_listener, daemon=True).start()
    app.run(port=8080)