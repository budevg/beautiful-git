beautiful-git
=============

Improve your code quality by adding meaningful commit messages

Reading the history of the code is one of the most important tools
to understand it's developers reasoning and to find answers to the
one true question you will ask each time you've encountered a bug:
*Why GOD ... Why*

Unfortunately due to time pressure, lack of education and excessive
beer drinking we may end up with code repositories that contain
commit messages below the specified standard.

This tool which is based on AI algorithm can be applied to any existing
git repository. It rewrites the commits history by specifying meaningful
commit messages.

For example:

```
>> git clone https://github.com/docker/libcontainer.git
>> cd libcontainer
>> git log --oneline | head -10
318d845 Merge pull request #172 from cf-guardian/create-api
24e7b86 Remove erroneous reference to 'path' in description and error list;
395d842 Merge pull request #174 from vmarmol/no-sleep
40d371a Merge pull request #173 from crosbymichael/device-ownership
d2a3ff2 Merge pull request #170 from soundcloud/syncpipe-read-before-close-child
55f3560 Get UID and GID for device nodes
1faa2b5 syncpipe: read from parent before reporting error
2636848 Remove sampling from libcontainer CPU stats.
55430d0 Merge pull request #166 from crosbymichael/api-update
d6348ae Update container to have ID provided by the user
```
```
>> beautiful-git.py
Amazing physics going on...
Rewrite 318d845931f5af3ece31fcea42d003ec08538dcc (606/606)
Ref 'refs/heads/master' was rewritten
>> git log --oneline | head -10
d3253a1 Fix the fixes
c65bc33 Does anyone read this? I'll be at the coffee shop accross the street.
0a7dc38 someday I gonna kill someone for this shit...
2c6f39e Fixing Sarah's bugs.
206fea8 small is a real HTML tag, who knew.
ef22717 bifurcation
2afd5ef JASON, WE WENT OVER THIS. C++ IO SUCKS.
4bc3d3f debug line test
a0e697b rats
128774e I expected something different.
```
