from app import app, db
import os

def apprun():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    

if __name__ == "__main__":
    apprun()