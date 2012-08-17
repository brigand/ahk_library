---
title: Core.firstValid(a\*)
layout: post
---
# {{ page.title }} 

Get the first `true` parameter passed.

---

## Parameters

### a\*

Any number of parameters may be passed.

{% highlight ahk %}

    Core.firstValid(0, 0, 3, 5) ; Returns 3

{% endhighlight %}

---
## Return Value

In left-to-rigbt order, the first parameter to bee seen as `true`.  If none of them qualify, and empty string is returned.  Because of this, you can check if any of them are valid by using an `if` statement.

{% highlight ahk %}

    if not Core.firstValid(0, "", false, an_undefined_variable)
        MsgBox, Sorry... none of these are true.

{% endhighlight %}

---
## Explaination:

### What is true?

The following are false, everything else is true.

 - `""` (an empty string)
 - 0
 - false

Note that the strings `"0"` and `"false"` both evaluate to `true`.



---
## Examples:

{% highlight ahk %}

    #Include <lib_CORE>
    
    ; Try to load a username from various locations
    FileRead, LocalName, Name.txt
    FileRead, DocsName, %A_MyDocuments%\Name.txt
    FileRead, GlobalName, %A_ProgramFiles%\MyApp\Name.txt
    
    ; Use the most specific name we can find
    ; or use "User" as a default
    MsgBox % "Hi " . Core.firstValid(LocalName, DocsName, GlobalName, "User")

{% endhighlight %}
