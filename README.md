# Build Number Provider

```zsh
source venv/bin/activate
pip install -r requirements.txt

# Debug
python -m flask --app app run --debug 

# Release
python -m flask --app app run --port 18750
```