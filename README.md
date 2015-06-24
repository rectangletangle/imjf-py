imjf-py
========

The official Python client for [www.isMyJsFucked.com](http://www.ismyjsfucked.com/).

## Usage
`is_my_js_fucked` takes URLs and determines if their JavaScript code is broken. Returning `True` indicates that at least one URL is confirmed for being broken. `None` indicates that at least one URL is unknown. `False` indicates everything is ok. An `IMJFException` will be raised if something goes wrong. More information can be found at [www.isMyJsFucked.com/api/](http://www.ismyjsfucked.com/api/).

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
