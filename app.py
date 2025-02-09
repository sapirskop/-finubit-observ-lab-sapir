from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response, request
import time

app = Flask(__name__)

# Define Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
RESPONSE_TIME = Histogram(
    'response_time_seconds', 'Response time in seconds', ['endpoint'],
    buckets=[0.005, 0.01, 0.1, 0.5, 1, 2, 5, 10, float("inf")]
)

@app.route('/metrics')
def metrics():
    """Expose Prometheus metrics"""
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)

@app.route('/deposit', methods=['POST'])
def deposit():
    print("Received a request to /deposit")  # Debugging log
    REQUEST_COUNT.labels(method='POST', endpoint='/deposit').inc()
    
    start_time = time.time()
    time.sleep(1)  # Simulate processing time
    duration = time.time() - start_time  # Calculate response time
    
    RESPONSE_TIME.labels(endpoint="/deposit").observe(duration)  # Log response time
    
    return {"message": "Deposit successful"}

@app.route('/withdraw', methods=['POST'])
def withdraw():
    print("Received a request to /withdraw")  # Debugging log
    REQUEST_COUNT.labels(method='POST', endpoint='/withdraw').inc()
    
    start_time = time.time()
    time.sleep(3)  # Simulate slow processing
    duration = time.time() - start_time  # Calculate response time
    
    RESPONSE_TIME.labels(endpoint="/withdraw").observe(duration)  # Log response time
    
    return {"message": "Withdrawal processed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
