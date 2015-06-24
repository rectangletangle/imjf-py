imjf-py
========

The official Python client for [www.isMyJsFucked.com](http://www.ismyjsfucked.com/)

## Usage
```python
>>> from imjf import is_my_js_fucked
>>> is_my_js_fucked('http://www.ismyjsfucked.com/tests/exception.html')
True
>>> is_my_js_fucked('http://www.ismyjsfucked.com/tests/ok.html')
False
```

## Dependencies
* [requests](http://docs.python-requests.org/)

## Installation
```sh
$ pip install imjf
```
