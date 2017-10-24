# ArithmeticTranslator
A simple arithmetic translator to quaternaries

2017 编译原理作业 15231177 王辰昱

To try this translator,

use command line:

```bash
cd ArithmeticTranslator/
python main.py %InputExpression%
```

For example, clone this repository and enter:

```bash
cd ArithmeticTranslator/
python main.py test_texts/syntax_test3.txt
```

from input
```
(a+b+c)*c
```

You will get (`a` at 1, `b` at 2, `c` at 4, `(a+b+c)` at 5, `(a+b+c)*c` at 6 ):

```
ADD 1 2 3
ADD 3 4 5
MULT 5 4 6
```

