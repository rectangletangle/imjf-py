imjf-py
========

The official Python client for [www.isMyJsFucked.com](http://www.ismyjsfucked.com/). This service is ideal for setting
up quick and dirty smoke tests on your most important URLs.

## Usage
`ismyjsfucked` determines if the JavaScript at a URL is broken. Returning `True` indicates that the JavaScript has
thrown an exception, or is somehow invalid. `False` signifies that everything is ok. `None` is returned when the state
of the JavaScript is unknown, or the URL's status code implies failure, i.e., 4XX or 5XX. An `IMJFException` will be
raised if something goes awry, e.g., client, or network errors. More information can be found at
[www.isMyJsFucked.com/api/](http://www.ismyjsfucked.com/api/).

```python
>>> from imjf import ismyjsfucked
>>> ismyjsfucked('http://www.ismyjsfucked.com/tests/exception.html')
True
>>> ismyjsfucked('http://www.ismyjsfucked.com/tests/ok.html')
False
>>> urls = ['www.ismyjsfucked.com/tests/ok.html', 'www.ismyjsfucked.com/tests/exception.html']
>>> ismyjsfucked(urls) # returns `True`, because at least one URL is fucked
True
```

## Installation
```sh
$ pip install imjf
```

## Dependencies
* Python 2 or 3
* [requests](http://docs.python-requests.org/)
