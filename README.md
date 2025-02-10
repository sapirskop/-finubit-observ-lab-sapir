## Usage

1. Install
- git Bash 
- Python 
- Docker & Docker Compose 
- Prometheus & Grafana 

 Check if install:
```bash python --version```
```bash docker --version```
```bash docker-compose --version```

2. Clone the project
```bash
  git clone https://github.com/barkai36/finubit-observ-lab.git
```
3. Go to project directory
```bash
cd finubit-observ-lab
```
4. Run project
```bash
docker-compose up --build 
```

## Testing
The project will run two services: 'deposit' and 'core'.


The 'deposit' service represent a front-end service to customers.

The 'core' service represent a back-end that is not reached to customer.

The following API requests are available with 'deposit':

http://localhost:5000/deposit
Deposit ammount of money into the account.

Example:
```bash
curl --location 'http://localhost:5000/deposit' \
--header 'Content-Type: application/json' \
--data '{
    "amount":100
}'
```

http://localhost:5000/withdraw
Withdraw amount of money from the account
Example:
```bash
curl --location 'http://localhost:5000/withdraw' \
--header 'Content-Type: application/json' \
--data '{
    "amount":100
}'
```

5. Run Prometheus using Docker:

```bash docker run -d --name=prometheus -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/Prometheus```

- Open http://localhost:9090
- Go to http://localhost:9090/targets 
Ensure flask-app is UP

Prometheus configuration (prometheus.yml):

global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['192.168.68.62:5000']

  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

```bash docker restart prometheus```

6.  Install and Start Grafana
Run Grafana using Docker:

```bash docker run -d --name=grafana -p 3000:3000 grafana/grafana```

Open Grafana:
http://localhost:3000
Login credentials:

Username: admin
Password: admin (change  the password)

7.Add Prometheus as a Data Source in Grafana

Grafana > "Configuration" > "Data Sources"
Click "Add Data Source">Select "Prometheus"
Set URL to:
http://localhost:9090

Click "Save & Test"


