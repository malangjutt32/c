#coding=utf-8
import platform

bit=platform.architecture()[0]

if bit=="64bit":
    import jatt
    jatt.sec1()
elif bit=="32bit":
    import jatti
    jatti.sec1()
