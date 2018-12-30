# word-counter

A word-counter project for Asella

## Requirement

![requirement](requirement.jpg)

## Prerequisite

* To install virtualenv
```bash
sudo pip install virtualenv
```
* To make an environment
```bash
virtualenv -p python3 [env_name]
```
* Enable the environment
```bash
source [env_name]/bin/activate
```
* Disable the environment
```bash
deactivate
```
* Install dependencies
```bash
pip install -r requirements.txt
```

## Execute

### Shell

```bash
python csv_word_counter.py data_science_bootcamps.csv \
    --column_name=MESSAGES \
    --include_pattern='PhD|12'\
    --exclude_pattern='\d+'
```

### Web server

```bash
python flask_upload.py
```