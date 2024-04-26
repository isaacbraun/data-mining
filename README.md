# Data Mining (CPTR-524) Course Work

## Usage
### Create virtual environment and activate:
```bash
python3 -m venv .venv
source .venv/bin/activate
# or if in home terminal
venv-a
```

### Install requirements:
```bash
pip install -r requirements.txt
```

#### For Win
```bash
pip install -U pip setuptools wheel
pip install -U spacy
```

#### For MacOS
```bash
pip install -U pip setuptools wheel
pip install -U 'spacy[apple]'
```

#### Win TensorFlow Cuda Fix
https://github.com/tensorflow/tensorflow/issues/63362
```bash
export NVIDIA_DIR=$(dirname $(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)")))
export LD_LIBRARY_PATH=$(echo ${NVIDIA_DIR}/*/lib/ | sed -r 's/\s+/:/g')${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

### Write requirements:
```bash
pip freeze > requirements.txt
```
