
import base64

def handler(event):
    text = event.get("text", "")
    return {
        "statusCode": 200,
        "body": f"📢 Received text: {text}"
    }
