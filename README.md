# Build Number Provider

## Setup

```zsh
source venv/bin/activate
pip install -r requirements.txt

# Debug
python -m flask --app app run --debug 

# Release
python -m flask --app app run --port 18750
```

## Usage
```zsh
[POST] /v1/build_number
{
    "latest_build_number": 100
}

# Response
{
    "next_build_number": 101
}
```