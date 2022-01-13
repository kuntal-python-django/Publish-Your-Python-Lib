# Publish Your Own Python Library
-----


# To build and test in Local

- build command
```
    > python setup.py pytest [optional]

    > python setup.py sdist bdist_wheel
``` 

- To install from your Local System
```
    pip install /path/to/dist/wheelfile.whl

    > pip install /home/kuntal/research/Publish-Your-Python-Lib/Package_0/dist/kuntal_test_lib-0.0.1-py3-none-any.whl

    > entry_call    [ define in entry_points ]
```


# Steps To Upload in PyPi
```
    > pip install twine
    > twine upload dist/*
    
    > twine upload --repository testpypi dist/*    [ upload cmd for test PyPi]
```
## _:Notes:_
1. You will be asked to provide your username and password. Provide the credentials you used to register to PyPi earlier
2. https://pypi.org/project/YOURPACKAGENAME/    [your package online]


## To install it from pypi
```
    > pip install kuntal-test-lib-0.0.1
    
    > pip install https://test.pypi.org/project/kuntal-test-lib/  [install from test PyPi]
```


## How to import and use [with in dist folder]
```
    import mypythonlib
    from mypythonlib import myfunctions
```


-------------
# Technical Help
-------------

- classifiers
```
classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
```

-  entry_points
```
    entry_points = {
        'my_ep_group_id': [
            'my_ep_func = myns.mypkg.mymodule:the_function'
        ]
    }
```


### - setup.cfg

This is a short one. Create a new file called “setup.cfg”. If you have a description file (and you definitely should!), you can specify it here


### Open source License
```
    https://opensource.org/licenses/
```
