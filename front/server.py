from flask import Flask, request
from prometheus_client import start_http_server, Counter, Summary, Histogram
import time

app = Flask(__name__)

# הגדרת מדדים
REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_DURATION = Summary('http_request_duration_seconds', 'Request duration in seconds', ['method', 'endpoint'])
ERRORS = Counter('http_requests_errors_total', 'Total HTTP errors', ['method', 'endpoint'])
WITHDRAW_DURATION = Histogram('withdraw_duration_seconds', 'Duration of withdraw operation')

# יצירת נתיב Deposit
@app.route('/deposit', methods=['POST'])
def deposit():
    start_time = time.time()
    # לוגיקת עיבוד עבור Deposit
    REQUESTS.labels(method='POST', endpoint='/deposit').inc()
    REQUEST_DURATION.labels(method='POST', endpoint='/deposit').observe(time.time() - start_time)
    return 'Deposit done'

# יצירת נתיב Withdraw
@app.route('/withdraw', methods=['POST'])
def withdraw():
    start_time = time.time()
    time.sleep(3)  # הדמיית זמן עיבוד איטי
    REQUESTS.labels(method='POST', endpoint='/withdraw').inc()
    REQUEST_DURATION.labels(method='POST', endpoint='/withdraw').observe(time.time() - start_time)
    WITHDRAW_DURATION.observe(time.time() - start_time)  # מדידת זמן עיבוד עבור Withdraw
    return 'Withdraw done'

# חשיפה של המדדים
@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8000)  # תחילת שרת Prometheus
    app.run(host='0.0.0.0', port=5000)
