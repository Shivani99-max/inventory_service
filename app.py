from flask import Flask, jsonify
from api.routes import inventory_bp

app = Flask(__name__)

app.register_blueprint(inventory_bp, url_prefix="/v1/inventory")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=18083, debug=True)

@app.route("/health", methods=["GET"])
def health_check():  
  

  """
Basic health check endpoint for monitoring and Docker/K8s readiness probes.
"""
  return jsonify({
    "status": "ok",
    "service": "inventory-service",
    "message": "Service is healthy and running"
    }), 200