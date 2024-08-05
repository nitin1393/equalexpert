from app import create_app
import logging
import os

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("app.log"),
                            logging.StreamHandler()
                        ])
setup_logging()
app = create_app()

port_number = os.environ.get('port_number')

if __name__ == '__main__':
    if not port_number:  # This handles both None and empty string
        app.run(debug=True, host="0.0.0.0", port=8080)
    else:
        app.run(debug=True, host="0.0.0.0", port=int(port_number))
