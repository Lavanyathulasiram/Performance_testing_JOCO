import json
import time
from datetime import datetime
from utils.excel_writer import update_excel
import websocket

def run_ws(ws_url, headers, payload, result_container, results, start_time, file_path):
    def on_open(ws): ws.send(json.dumps(payload))

    def on_message(ws, message):
        #print(f"WebSocket Response: {message[:100]}...")
        try:
            data = json.loads(message)
            status = data.get("status", "").lower()
            if status in ["complete", "timeout"]:
                result_container["Status"] = status
                result_container["Message"] = message[:1000]
                result_container["End Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result_container["Response Time (ms)"] = round((time.time() - start_time) * 1000, 2)
                ws.close()
        except Exception as e:
            print("Error parsing message:", e)

    def on_error(ws, error): print("WebSocket Error:", error)

    def on_close(ws, code, msg):
        print(f"WebSocket closed ({code})")
        results.append(result_container)
        update_excel(file_path, results)

    ws = websocket.WebSocketApp(
        ws_url,
        header=[f"{k}: {v}" for k, v in headers.items()],
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
