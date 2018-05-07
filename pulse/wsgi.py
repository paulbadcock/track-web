import os
from pulse import create_app
import yaml

port = int(os.getenv("PORT", 5000))
environment = os.getenv("PULSE_ENV", "development")
app = create_app(environment)

if __name__ == "__main__":
    if environment == "development":
        app.debug = True

    app.run(port=port)
