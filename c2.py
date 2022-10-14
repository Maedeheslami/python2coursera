Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def computepay(h,r):
...     if h > 40:
...         p = 1.5 * r * (h - 40) + (40 *r)
...     else:
...         p = h * r
...     return p
...     
... hrs = input("Enter Hours:")
... hr = float(hrs)
... rphrs = input("Enter rate per hour:")
... rphr = float(rphrs)
... 
... p = computepay(hr,rphr)
