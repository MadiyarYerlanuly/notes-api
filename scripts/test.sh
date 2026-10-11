#!/usr/bin/env bash
set -euo pipefail

export PORT=9090
python3 app.py &
SERVER_PID=$!

cleanup() {
    kill $SERVER_PID 2>/dev/null || true
}
trap cleanup EXIT

sleep 1

RESP1=$(curl -s http://localhost:9090/)
if [ "$RESP1" != "Hello, World!" ]; then
    echo "Test 1 failed"
    exit 1
fi

HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9090/healthz)
if [ "$HTTP_STATUS" != "200" ]; then
    echo "Test 2 failed"
    exit 1
fi

RESP3=$(curl -s http://localhost:9090/notes)
if [[ "$RESP3" != *"купить молоко"* ]]; then
    echo "Test 3 failed"
    exit 1
fi

echo "TESTS: 3/3"
