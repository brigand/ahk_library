---
title: Math.changeBase(n, base = 10)
layout: post
---
# {{ page.title }} 

Change a number from base 10 to another base.

---

## Parameters

### n

Any base 10 number.

### base

The new base can be any integer from 2 to 16 (binary to hex).  Choosing the default (base 10) causes no change, other than rounding floating point numbers.

---
## Return Value

A string representation of the number in the chosen base.

---
## Examples:

{% highlight ahk %}

#Include <lib_core>

; Simple example

MsgBox % Math.changeBase(60, 3) ; Shows 2020

; Asking the user for input

InputBox inp,, Give me a number!
InputBox newbase,, And a base!

inp_rebased := Math.changeBase(inp, newbase)

MsgBox The number %inp% in base %newbase% is %inp_rebased%

{% endhighlight %}
