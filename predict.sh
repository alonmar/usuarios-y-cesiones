#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "monactivo": 0,
   "meansales": 0,
   "meancesiones": 0,
   "proyecsales": 0,
   "proyecbuys": 0
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
