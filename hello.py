# -*- coding: utf-8 -*-
import ctypes

soName = 'hello.so'
fn = ctypes.CDLL(soName)

fn.hello()
