# Create a virtual environment
python -m venv .

# Activate the environment
./venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Export Flash environment variable
export FLASK_APP=server.py

# Run the server
flask run