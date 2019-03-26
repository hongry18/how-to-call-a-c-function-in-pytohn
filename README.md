# how to call a c function in python

## 1. hello.c
```
#include <stdio.h>

int hello() {
    printf("hello");
    return 0;
}
```

## 2. compile
```
gcc -shared -o hello.so hello.c
```

## 3. call a C function in python
```
import ctypes

fn = ctypes.CDLL('hello.so')
fn.hello()
```
