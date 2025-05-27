from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from dotenv import load_dotenv


from utils import get_weather_data, city_name
from openai_reporter import ai_reporter

load_dotenv()
app = Flask(__name__)
REQUESTS = Counter("app_requests_total", "Total number of requests")

@app.route('/weather', methods=['GET'])
def weather():
    REQUESTS.inc()
    weather_data = get_weather_data(city_name)
    report = ai_reporter(city_name, weather_data)
    return jsonify({
        "city": city_name,
        "temperature": weather_data['temperature'],
        "weather": weather_data['weather'],
        "report": report
    })
@app.route('/metrics', methods=['GET'])
def metrics():
    REQUESTS.inc()
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)