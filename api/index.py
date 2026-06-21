from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔴 YOU WILL PASTE TELEMETRY HERE
TELEMETRY_DATA = [
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 218.12,
    "uptime_pct": 97.405,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 180.91,
    "uptime_pct": 97.43,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 186.24,
    "uptime_pct": 98.112,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 184.36,
    "uptime_pct": 97.473,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 132.75,
    "uptime_pct": 97.322,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 184.04,
    "uptime_pct": 97.218,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 189.96,
    "uptime_pct": 98.226,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 126.49,
    "uptime_pct": 98.488,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 125.2,
    "uptime_pct": 98.922,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 149.3,
    "uptime_pct": 98.225,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 155.08,
    "uptime_pct": 99.438,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 149.48,
    "uptime_pct": 99.339,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 224.41,
    "uptime_pct": 98.934,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 118.32,
    "uptime_pct": 98.828,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 119.28,
    "uptime_pct": 98.183,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 151.92,
    "uptime_pct": 97.752,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 211.88,
    "uptime_pct": 98.141,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 177.79,
    "uptime_pct": 98.934,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 166.32,
    "uptime_pct": 98.932,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 146.63,
    "uptime_pct": 97.75,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 209.59,
    "uptime_pct": 98.78,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 104.56,
    "uptime_pct": 99.22,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 203.81,
    "uptime_pct": 97.856,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 191.77,
    "uptime_pct": 99.194,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 217.79,
    "uptime_pct": 97.149,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 202.26,
    "uptime_pct": 98.982,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 147.51,
    "uptime_pct": 99.333,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 120.52,
    "uptime_pct": 98.161,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 212.74,
    "uptime_pct": 98.144,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 198.59,
    "uptime_pct": 98.982,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 168.6,
    "uptime_pct": 98.673,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 152.41,
    "uptime_pct": 98.138,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 200.95,
    "uptime_pct": 98.245,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 200.46,
    "uptime_pct": 99.251,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 224.75,
    "uptime_pct": 98.596,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 156.28,
    "uptime_pct": 98.872,
    "timestamp": 20250312
  }
]

@app.post("/api/latency")
async def latency(request: Request):
    body = await request.json()
    regions = body["regions"]
    threshold = body["threshold_ms"]

    result = []

    for region in regions:
        records = [r for r in TELEMETRY_DATA if r["region"] == region]

        lat = [r["latency_ms"] for r in records]
        up = [r["uptime_pct"] for r in records]

        result.append({
            "region": region,
            "avg_latency": float(np.mean(lat)),
            "p95_latency": float(np.percentile(lat, 95)),
            "avg_uptime": float(np.mean(up)),
            "breaches": sum(1 for x in lat if x > threshold)
        })

    return {"regions": result}
