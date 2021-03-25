# hypeme
hype yourself up!

## Installation

```
pip install hypeme
```

## Usage

tired of ur boring old print statement?

```python
>>> print('yeah')
yeah :(
```

as we like to say, hype yourself up!

```python
>>> import hypeme
>>> print('how?')
HOW?!!!!!!!
>>> print('oh wow i am a good and caring person')
OH WOW I AM A GOOD AND CARING PERSON!!
```

should work on most stuff!!

```python
>>> import numpy as np
>>> print(np.zeros((3,3)))
ARRAY([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])!!!!!!!!!
>>> print(np.array)
<BUILT-IN FUNCTION ARRAY>!!!!!!!!!!
>>> print([1, 2, 3, 'birds', set('and'), b'bees'])
[1, 2, 3, 'BIRDS', {'A', 'D', 'N'}, B'BEES']!!!!!!!!!
```

if it doesn't it's still nice about it

```python
class NoRepr:
	def __repr__(self):
		raise Exception('You cant represent me!')

>>> print(NoRepr())
IF I CANT YELL IT THEN I WONT PRINT IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
>>> hypeme.relax()
ok sorry i just get excited for you is all

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jonny/git/hypeme/hypeme/__init__.py", line 34, in relax
    builtins.ye_olde_print(_LAST_PRINT)
  File "<stdin>", line 3, in __repr__
Exception: You cant represent me!
```

and when you are fully hyped you can go back to the real world
```python
>>> hypeme.no_hyping()
smell ya later!
>>> print('so quiet in here all of a sudden')
so quiet in here all of a sudden
```



