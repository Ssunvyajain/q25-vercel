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
TELEMETRY_DATA = []

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
